from peewee import *
from datetime import date

db = SqliteDatabase('betsy.db', pragmas={'foreign_keys': 1})
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
    avatar_url = CharField(null=True, default="https://www.pngitem.com/pimgs/m/146-1468843_profile-icon-orange-png-transparent-png.png")

class Product(BaseModel):
    title = CharField(max_length=100)
    description = TextField(null=True)
    price_in_cents = IntegerField(constraints=[Check('price_in_cents >= 0')])
    qty = IntegerField(constraints=[Check('qty >= 0')])
    prod_id = AutoField()
    user = ForeignKeyField(User, backref='products', on_delete='CASCADE')
    date_added = DateField(default=date.today())

class Order(BaseModel):
    vendor = ForeignKeyField(User, backref='sales')
    buyer = ForeignKeyField(User, backref='purchases')
    product = ForeignKeyField(Product, backref='orders')
    qty = IntegerField(constraints=[Check('qty > 0')])
    date = DateField(default=date.today())
    order_id = AutoField()

class Product_image(BaseModel):
    image_id = AutoField()
    product = ForeignKeyField(Product, backref='images', on_delete='CASCADE')
    image_url = CharField(null=True)

class Tag(BaseModel):
    name = CharField(max_length=50)
    products = ManyToManyField(Product, backref='tags')

ProductTag = Tag.products.get_through_model()

def create_tables():
    with db:
        db.create_tables([User, Product, Order, Product_image, Tag, ProductTag])

create_tables()