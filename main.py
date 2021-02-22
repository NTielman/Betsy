import os
from flask import Flask, redirect, render_template, request, session, url_for, flash, abort
from helpers import verify_password, verify_user
from queries import *
from cart import Cart

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def frontpage(user=False):
    if "user" in session:
        user = session["user"]
    featured_products = get_newest_products()
    return render_template("home_page.html", user=user, products=featured_products)

@app.route('/home/')
def home():
    return redirect(url_for("frontpage"))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_succesfull = verify_password(username, password)
        if login_succesfull:
            user = get_user(username)
            session["user"] = user
            return redirect(url_for("frontpage"))
        else:
            return redirect(url_for('login'))
    else:
        if "user" in session:
            return redirect(url_for("frontpage"))
        return render_template('log_in.html')

@app.route('/logout/')
def logout():
    if "user" in session:
        session.pop("user", None)
        flash("You have been logged out", 'info')
    return redirect(url_for("frontpage"))

@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        username = request.form["username"]
        fullname = request.form["full_name"]
        address = request.form["address"]
        bio = request.form["bio"]
        avatar_url = request.form["avatar_url"]
        password = request.form["password"]
        user_is_valid = verify_user(username, fullname, address, bio, avatar_url, password)
        if user_is_valid:
            user = get_user(username)
            session["user"] = user
            return redirect(url_for("frontpage"))
        else:
            return redirect(url_for('sign_up'))
    else:
        if "user" in session:
            return redirect(url_for("frontpage"))
        return render_template("sign_up.html")

@app.route('/my_profile/')
def my_profile():
    if "user" in session:
        user = session["user"]
        user_products = list_user_products(user["user_id"])
        user_sales = list_user_sales(user["user_id"])
        user_purchases = list_user_purchases(user["user_id"])
        return render_template('my_profile.html', user=user, products=user_products, sales=user_sales, purchases=user_purchases)
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/add_product/', methods=['GET', 'POST'])
def add_product():
    if "user" in session: #check if user is logged in
        if request.method == "POST":

            #create product instance
            title = request.form["title"]
            description = request.form["description"]
            price = request.form["price"]
            qty = request.form["qty"]
            user = session["user"]

            product = {
                "title": title,
                "description": description,
                "price_in_cents": float(price) * 100, #convert price to cents 
                "qty": qty,
                "user": user
            }

            product_id = add_product_to_catalog(product)

            if product_id:
                # add product images
                image_1 = request.form["image_1"]
                image_2 = request.form["image_2"]
                image_3 = request.form["image_3"]
                image_4 = request.form["image_4"]
                image_5 = request.form["image_5"]
                images = [image_1, image_2, image_3, image_4, image_5]

                if images: # if image list isn't empty
                    add_images_to_product(product_id, images)

                #add product tags
                tags = request.form["tags"]
                tag_list = tags.split(", ")
                
                if tag_list:
                    add_product_tags(product_id, tag_list)

                # return redirect to /product_page/<prod_id>
                return redirect(url_for('my_profile'))
            else:
                flash("Could not add product", 'error')
                return redirect(url_for('add_product'))
        else:  #method is GET
            return render_template("add_product.html")
    else:
        return redirect(url_for('login'))

@app.route('/product_page/<product_id>', methods=['GET', 'POST'])
def product_page(product_id):
    user_cart = Cart(session)
    product = get_product(product_id)

    if request.method == "POST":
        quantity = request.form["quantity"]
        user_cart.add_product(product_id, quantity, False)
        flash("Item added to cart", 'info')
        return redirect(url_for("product_page", product_id=product_id, _method='GET'))

    if product:
        product_tags = get_product_tags(product_id)
        product_images = get_product_images(product_id)
        return render_template("product_page.html", product=product, product_images=product_images, product_tags=product_tags)
    else:
        abort(404)

@app.route('/user_page/<username>')
def user_page(username):
    other_user = get_user(username)
    if other_user:
        user_products = list_user_products(other_user.user_id)
        return render_template("user_page.html", other_user=other_user, products=user_products)
    else:
        abort(404)

@app.route('/products/<tag>')
def search_products_by_tag(tag):
    tagged_products = list_products_per_tag(tag)
    return render_template("products_page.html", tag=tag, products=tagged_products)

@app.route('/search/')
def search_products():
    query = request.args.get("query")
    products = search(query)
    return render_template("search.html", query=query, products=products)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# my products - list all my products. (possible to edit), user products- list all users products

if __name__ == "__main__":
    app.run(debug=True)