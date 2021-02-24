__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Transaction, ProductImage, Tag
import peewee
from peewee import fn
from flask import flash
from playhouse.shortcuts import model_to_dict, dict_to_model

def get_user_password(user_name):
    '''finds username and returns user passwords from database'''
    try:
        user = User.get(User.username == user_name)
        return user.password
    except peewee.DoesNotExist:
        return False

def create_user(user_name, user_full_name, user_address, user_bio, user_avatar, user_password):
    '''adds a user to database'''
    try:
        return User.create(
            username=user_name, full_name=user_full_name, address=user_address, bio=user_bio, avatar_url=user_avatar, password=user_password 
        )
    except peewee.PeeweeException:
        return False

def get_user(user_name):
    '''finds and returns a user dictionary from database'''
    try: 
        user = User.get(User.username == user_name)
        return model_to_dict(user)  #converts DB user to dictionary
    except peewee.DoesNotExist:
        return False

def edit_user(user_id, name, address, bio, avatar_url):
    '''modifies and updates a user info'''
    try:
        user = User.get_by_id(user_id)

        if name:
            user.full_name = name
        if address:
            user.address = address
        if bio:
            user.bio = bio
        if avatar_url:
            user.avatar_url = avatar_url

        user.save()
        return model_to_dict(user)
    except peewee.PeeweeException:
        return False

def get_product(product_id):
    '''finds and returns a product dictionary from database'''
    try:
        product = Product.get_by_id(product_id)
        return model_to_dict(product, backrefs=True)
    except peewee.DoesNotExist:
        return False

def get_product_images(product_id):
    '''returns a list of product_images if any'''
    product = Product.get_by_id(product_id)
    images = [image.image_url for image in product.images ] 
    return images

def get_product_tags(product_id):
    '''returns a list of tags associated to a product if any'''
    product = Product.get_by_id(product_id)
    tags = [tag.name for tag in product.tags ] 
    return tags

def get_newest_products():
    '''returns 10 products in database sorted by date added'''
    query = (Product
             .select()
             .order_by(Product.date_added.desc())
             .limit(10))
    products = [model_to_dict(product) for product in query]
    return products

def get_all_products():
    '''returns all products from database'''
    query = Product.select()
    products = [model_to_dict(product) for product in query]
    return products

def list_user_products(user_id):
    '''returns a list of products a user is selling'''
    user = User.get_by_id(user_id)
    products = [model_to_dict(product, backrefs=True) for product in user.products]
    return products

def list_user_sales(user_id):
    '''returns a list of sales for a given user'''
    user = User.get_by_id(user_id)
    sales = [model_to_dict(sale, backrefs=True) for sale in user.sales]
    return sales

def list_user_purchases(user_id):
    '''returns a list of purchases made by a given user'''
    user = User.get_by_id(user_id)
    purchases = [model_to_dict(purchase, backrefs=True) for purchase in user.purchases]
    return purchases

def add_product_to_catalog(product_info):
    '''creates and adds a product to user's profile'''
    try:
        product = dict_to_model(Product, product_info)
        product.save()
        return product.prod_id
    except peewee.PeeweeException:
        return False

def add_images_to_product(product_id, image_list):
    '''adds images to a product'''
    product = Product.get_by_id(product_id)

    #set first image as product thumbnail
    product.thumbnail = image_list[0]
    product.save()
    
    for image_url in image_list:
        if image_url:  #if image field isn't empty
            prod_image = ProductImage(product=product, image_url=image_url)
            prod_image.save()

def add_product_tags(product_id, tag_list):
    '''adds tags to a product'''
    product = Product.get_by_id(product_id)

    for tag in tag_list:
        if tag:
            product_tag, created = Tag.get_or_create(name=tag.lower())
            product.tags.add(Tag.get(Tag.name == tag.lower()))

def list_products_per_tag(tag_name):
    '''returns a list of products associated with a given tag'''
    tag = Tag.get(Tag.name == tag_name)
    products = [model_to_dict(product) for product in tag.products]
    return products

def search(term):
    '''returns a list of products whose name or description contains a given term'''
    search_term = term.lower()
    query = (Product
             .select()
             .where(fn.Lower(Product.title).contains(search_term) | fn.Lower(Product.description).contains(search_term)))
    products = [model_to_dict(product) for product in query]
    return products

def checkout(buyer_id, cart):
    '''adds purchase info to transactions database'''
    #note to docent: this function replaces the purchase_product function from the Winc assignment
    try: 
        buyer = User.get_by_id(buyer_id)
        for item in cart:
            quantity = item['quantity']
            product = Product.get_by_id(item['id'])
            vendor = product.vendor

            if product.qty > quantity:
                Transaction.create(vendor=vendor, buyer=buyer, product=product, qty=quantity, product_thumb_url=product.thumbnail, prod_title=product.title, buyer_name=buyer.username, vendor_name=vendor.username)
                product.qty -= quantity
                product.save()
            else:
                flash(f"Could not order '{product.title}'. Not enough in stock", 'error')
        return True
    except peewee.PeeweeException:
        return False 

def edit_product(product_id, title, description, price, qty, thumbnail):
    '''modifies and updates a product info'''
    #note to docent: this function replaces the update_stock function from the Winc assignment
    try:
        product = Product.get_by_id(product_id)

        if title:
            product.title = title
        if description:
            product.description = description
        if price:
            product.price_in_cents = float(price) * 100
        if qty:
            product.qty = int(qty)
        if thumbnail:
            product.thumbnail = thumbnail

        product.save()
        return model_to_dict(product)
    except peewee.PeeweeException:
        return False

def remove_product(user_id, product_id):
    '''removes a product from database'''
    user = User.get_by_id(user_id)
    product = Product.get_by_id(product_id)
    if product.vendor == user:
        product_deleted = product.delete_instance()
        return product_deleted
    else:
        return False