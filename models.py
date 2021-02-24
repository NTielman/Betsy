from peewee import *
import os
from datetime import date

# Ensure database "betsy.db" is created in current folder
full_path = os.path.realpath(__file__)
file_dir = os.path.dirname(full_path)
db_path = os.path.join(file_dir, 'betsy.db')

db = SqliteDatabase(db_path, pragmas={'foreign_keys': 1})
# Ensure foreign-key constraints are enforced.

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = AutoField()
    password = CharField()
    username = CharField(unique=True, max_length=100)
    full_name = CharField()
    address = CharField()
    bio = TextField(null=True, default="Hi, i'm a happy Betsy user.")
    avatar_url = CharField(null=True)

class Product(BaseModel):
    title = CharField(max_length=100)
    description = TextField(null=True)
    price_in_cents = IntegerField(constraints=[Check('price_in_cents >= 0')])
    qty = IntegerField(constraints=[Check('qty >= 0')])
    prod_id = AutoField()
    vendor = ForeignKeyField(User, backref='products', on_delete='CASCADE')
    date_added = DateField(default=date.today())
    thumbnail = CharField(null=True)

class Transaction(BaseModel):
    vendor = ForeignKeyField(User, backref='sales', on_delete='SET NULL', null=True) 
    buyer = ForeignKeyField(User, backref='purchases', on_delete='SET NULL', null=True)
    product = ForeignKeyField(Product, backref='orders', on_delete='SET NULL', null=True)
    qty = IntegerField(constraints=[Check('qty > 0')])
    date = DateField(default=date.today())
    trans_id = AutoField()
    # if product or user is modified or deleted from db we should still 
    # be able to view some of their info in (existing) orders 
    # by storing them as order details (below)
    product_thumb_url = CharField(null=True) 
    prod_title = CharField(max_length=100)
    buyer_name = CharField(max_length=100)
    vendor_name = CharField(max_length=100)

class ProductImage(BaseModel):
    img_id = AutoField()
    product = ForeignKeyField(Product, backref='images', on_delete='CASCADE')
    image_url = CharField()

class Tag(BaseModel):
    name = CharField(max_length=50, unique=True)
    products = ManyToManyField(Product, backref='tags')

ProductTag = Tag.products.get_through_model()

def create_tables():
    with db:
        db.create_tables([User, Product, Transaction, ProductImage, Tag, ProductTag])