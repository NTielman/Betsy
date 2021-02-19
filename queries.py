__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Order, Product_image, Tag
import peewee
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
    '''finds and returns a user object from database'''
    user = User.get(User.username == user_name)
    return model_to_dict(user)  #converts DB user to dictionary

# def search(term):
#     ...

def list_user_products(user_id):
    '''returns a list of products a user is selling'''
    user = User.get(User.user_id == user_id)
    products = [model_to_dict(product) for product in user.products]
    return products

def list_user_sales(user_id):
    '''returns a list of sales for a given user'''
    user = User.get(User.user_id == user_id)
    sales = [model_to_dict(sale) for sale in user.sales]
    return sales

def list_user_purchases(user_id):
    '''returns a list of purchases made by a given user'''
    user = User.get(User.user_id == user_id)
    purchases = [model_to_dict(purchase) for purchase in user.purchases]
    return purchases

# def list_products_per_tag(tag_id):
#     ...

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
    product = Product.get(Product.prod_id == product_id)

    for image_url in image_list:
        if image_url:  #if image field wasn't empty
            prod_image = Product_image(product=product, image_url=image_url)
            prod_image.save()

def add_product_tags(product_id, tag_list):
    '''adds tags to a product'''
    product = Product.get(Product.prod_id == product_id)

    for tag in tag_list:
        product_tag, created = Tag.get_or_create(name=tag.lower())
        product.tags.add(Tag.get(Tag.name == tag.lower()))

# def update_stock(product_id, new_quantity):
#     ...


# def purchase_product(product_id, buyer_id, quantity):
#     ...


# def remove_product(product_id):
#     ...