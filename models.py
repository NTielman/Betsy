import os
from peewee import *
from datetime import date

# Ensure database "betsy.db" is created in current folder
full_path = os.path.realpath(__file__)
file_dir = os.path.dirname(full_path)
db_path = os.path.join(file_dir, 'betsy.db')

db = SqliteDatabase(db_path, pragmas={'foreign_keys': 1})
# Pragmas ensure foreign-key constraints are enforced.


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = AutoField()
    username = CharField(unique=True, max_length=100)
    password = CharField()
    full_name = CharField()
    address = CharField()
    bio = TextField(null=True)
    avatar_url = CharField(null=True)


class Product(BaseModel):
    prod_id = AutoField()
    vendor = ForeignKeyField(User, backref='products', on_delete='CASCADE')
    title = CharField(max_length=100)
    qty = IntegerField(constraints=[Check('qty >= 0')])
    price_in_cents = IntegerField(constraints=[Check('price_in_cents >= 0')])
    description = TextField(null=True)
    thumbnail = CharField(null=True)
    date_added = DateField(default=date.today())


class Transaction(BaseModel):
    trans_id = AutoField()
    vendor = ForeignKeyField(User, backref='sales',
                             on_delete='SET NULL', null=True)
    buyer = ForeignKeyField(User, backref='purchases',
                            on_delete='SET NULL', null=True)
    product = ForeignKeyField(
        Product, backref='orders', on_delete='SET NULL', null=True)
    qty = IntegerField(constraints=[Check('qty > 0')])
    date = DateField(default=date.today())
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
    products = ManyToManyField(Product, backref='tags', on_delete='CASCADE')


ProductTag = Tag.products.get_through_model()


def create_tables():
    with db:
        db.create_tables([User, Product, Transaction,
                          ProductImage, Tag, ProductTag])
