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
    avatar_url = CharField(null=True, default="https://media.istockphoto.com/vectors/default-profile-picture-avatar-photo-placeholder-vector-illustration-vector-id1223671392?b=1&k=6&m=1223671392&s=612x612&w=0&h=5VMcL3a_1Ni5rRHX0LkaA25lD_0vkhFsb1iVm1HKVSQ=")

class Product(BaseModel):
    title = CharField(max_length=100)
    description = TextField(null=True)
    price_in_cents = IntegerField(constraints=[Check('price_in_cents >= 0')])
    qty = IntegerField(constraints=[Check('qty >= 0')])
    prod_id = AutoField()
    vendor = ForeignKeyField(User, backref='products', on_delete='CASCADE')
    date_added = DateField(default=date.today())
    thumbnail = CharField(null=True, default="http://cdn.shopify.com/s/files/1/0169/2660/5412/collections/placeholder-images-collection-1_large_807560ab-9024-46ea-ab0a-bb49df2b3bb8_1200x1200.png?v=1551259616")

class Transaction(BaseModel):
    vendor = ForeignKeyField(User, backref='sales')
    buyer = ForeignKeyField(User, backref='purchases')
    product = ForeignKeyField(Product, backref='orders')
    qty = IntegerField(constraints=[Check('qty > 0')])
    date = DateField(default=date.today())
    trans_id = AutoField()

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