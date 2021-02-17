from peewee import *
from datetime import date

db = SqliteDatabase('betsy.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = AutoField()
    password = CharField()
    username = CharField(unique=True)
    full_name = CharField()
    address = CharField()
    bio = TextField(default="Hi, i'm a happy Betsy user.")
    avatar_url = CharField(default="https://www.pngitem.com/pimgs/m/146-1468843_profile-icon-orange-png-transparent-png.png")

class Product(BaseModel):
    title = CharField()
    description = TextField()
    price_in_cents = IntegerField()
    qty = IntegerField()
    # tags,
    # images,
    prod_id = AutoField()
    user = ForeignKeyField(User, backref='products')
    date_added = DateField(default=date.today())

class Order(BaseModel):
    vendor = ForeignKeyField(User, backref='sales')
    buyer= ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    qty = IntegerField()
    date = DateField(default=date.today())
    order_id = AutoField()

def create_tables():
    with db:
        db.create_tables([User, Product, Order])

create_tables()