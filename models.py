from peewee import *
from datetime import date

# db = SqliteDatabase('betsy.db')
db = SqliteDatabase(':memory:')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    full_name = CharField()
    adress = CharField()
    bio = TextField()
    avatar_url = CharField()
    user_id = AutoField()
    password = CharField()

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