import os
from models import create_tables
from flask import Flask, redirect, render_template, request, session, url_for, flash, abort
from helpers import verify_password, verify_user
import queries
from cart import Cart

app = Flask(__name__)
app.secret_key = os.urandom(16)
# create_tables()  #if you make a py file to make fake accounrs add this line to the start of that file
# in readme to docenten when first running to initialise betsy db and create some fake users to test site functionality with the file run the make fake accounts file. and then run main.py

@app.route('/')
def frontpage():
    featured_products = queries.get_newest_products()
    return render_template("home_page.html", products=featured_products)

@app.route('/home/')
def home():
    return redirect(url_for("frontpage"))

@app.route('/sign_in/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_succesfull = verify_password(username, password)
        if login_succesfull:
            user = queries.get_user(username)
            session["user"] = user
            return redirect(url_for("frontpage"))
        else:
            return redirect(url_for('login'))
    else:
        if "user" in session:
            return redirect(url_for("frontpage"))
        return render_template('log_in.html')

@app.route('/sign_out/')
def logout():
    if "user" in session:
        session.pop("user", None)
        flash("You have been signed out", 'info')
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
            user = queries.get_user(username)
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
        user_products = queries.list_user_products(user["user_id"])
        user_sales = queries.list_user_sales(user["user_id"])
        user_purchases = queries.list_user_purchases(user["user_id"])
        return render_template('my_profile.html', user=user, products=user_products[:7], sales=user_sales[:7], purchases=user_purchases[:7])
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/edit_profile/', methods=['GET', 'POST'])
def edit_profile():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            name = request.form["full_name"]
            address = request.form["address"]
            bio = request.form["bio"]
            avatar_url = request.form["avatar_url"]
            edit_successful = queries.edit_user(user["user_id"], name, address, bio, avatar_url)

            if edit_successful:
                session["user"] = edit_successful
                return redirect(url_for('my_profile'))
            else:
                flash("Something went wrong. Couldn't update your profile", 'error')
                return redirect(url_for('edit_profile'))

        else:  #method = "GET"
            return render_template("edit_profile.html", user=user)
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/edit_product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if "user" in session:
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            price = request.form["price"]
            qty = request.form["qty"]
            thumbnail = request.form["thumbnail"]

            edit_successful = queries.edit_product(product_id, title, description, price, qty, thumbnail)

            if edit_successful:
                return redirect(url_for("my_products"))
            else:
                flash("Something went wrong. Couldn't update product", 'error')
                return redirect(url_for("edit_product", product_id=product_id, _method='GET'))
        else:  #method = "GET"
            product = queries.get_product(product_id)
            if product:
                return render_template("edit_product.html", product=product)
            else:
                abort(404)
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/remove_product/<product_id>')
def remove_product(product_id):
    if "user" in session:
        user = session["user"]
        prod_removed = queries.remove_product(user["user_id"], product_id)
        if prod_removed:
            flash("Product has been removed", 'info')
        else:
            flash("Could not remove product", 'error')
        return redirect(url_for("my_products"))
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/add_product/', methods=['GET', 'POST'])
def add_product():
    if "user" in session:
        if request.method == "POST":

            title = request.form["title"]
            description = request.form["description"]
            price = request.form["price"]
            qty = request.form["qty"]
            user = session["user"]

            product = {
                "title": title,
                "description": description,
                "price_in_cents": float(price) * 100, #convert price to cents 
                "qty": int(qty),
                "vendor": user
            }

            product_id = queries.add_product_to_catalog(product) #if succesfull returns a product_id

            if product_id:
                # add product images
                image_1 = request.form["image_1"]
                image_2 = request.form["image_2"]
                image_3 = request.form["image_3"]
                image_4 = request.form["image_4"]
                image_5 = request.form["image_5"]
                images = [image_1, image_2, image_3, image_4, image_5]

                if images: # if image list isn't empty
                    queries.add_images_to_product(product_id, images)

                #add product tags
                tags = request.form["tags"]
                tag_list = tags.split(", ")
                
                if tag_list:
                    queries.add_product_tags(product_id, tag_list)

                return redirect(url_for("product_page", product_id=product_id, _method='GET'))
            else:
                flash("Could not add product", 'error')
                return redirect(url_for('add_product'))
        else:  #method is GET
            return render_template("add_product.html")
    else:
        return redirect(url_for('login'))

@app.route('/view_cart/', methods=['GET', 'POST'])
def view_cart():
    if "user" in session:
        cart = Cart(session)

        if request.method == "POST":
            buyer_id = session["user"]['user_id']
            order = queries.checkout(buyer_id, cart)

            if order:
                session.pop("cart", None)
                return redirect(url_for('success'))
            else:
                flash("Something went wrong, could not place your order", 'error')
                return redirect(url_for('view_cart'))

        else: # request = GET
            remove_product_id = request.args.get('remove_from_cart', '')
            changed_product_qty = request.args.get('change_quantity', '')
            quantity = int(request.args.get('quantity', 0))

            if remove_product_id:
                user_cart = cart.remove_product(remove_product_id)
                session['cart'] = user_cart
                session.modified = True
                return redirect(url_for('view_cart'))

            if changed_product_qty:
                user_cart = cart.add_product(changed_product_qty, quantity)
                session['cart'] = user_cart
                session.modified = True
                return redirect(url_for('view_cart'))

            return render_template('cart.html', cart=cart)
    else:
        flash("you must be logged in to view your cart", 'error')
        return redirect(url_for('login'))

@app.route('/checkout/success/')
def success():
    return render_template('success.html')

@app.route('/product_page/<product_id>', methods=['GET', 'POST'])
def product_page(product_id):
    if request.method == "POST":
        cart = Cart(session)
        quantity = int(request.form["quantity"])
        user_cart = cart.add_product(product_id, quantity)
        session['cart'] = user_cart
        session.modified = True
        flash("Item added to cart", 'info')
        return redirect(url_for("product_page", product_id=product_id, _method='GET'))
    else: # GET request
        product = queries.get_product(product_id)
        if product:
            product_tags = queries.get_product_tags(product_id)
            product_images = queries.get_product_images(product_id)
            return render_template("product_page.html", product=product, product_images=product_images, product_tags=product_tags)
        else:
            abort(404)

@app.route('/user_page/<username>')
def user_page(username):
    betsy_user = queries.get_user(username)
    if betsy_user:
        user_products = queries.list_user_products(betsy_user['user_id'])
        return render_template("user_page.html", betsy_user=betsy_user, products=user_products[:7])
    else:
        abort(404)

@app.route('/my_profile/my_products/')
def my_products():
    if "user" in session:
        user = session["user"]
        products = queries.list_user_products(user["user_id"])
        return render_template("my_products.html", products=products)
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/my_sales/')
def my_sales():
    if "user" in session:
        user = session["user"]
        sales = queries.list_user_sales(user["user_id"])
        return render_template("my_sales.html", sales=sales)
    else:
        return redirect(url_for('login'))

@app.route('/my_profile/my_purchases/')
def my_purchases():
    if "user" in session:
        user = session["user"]
        purchases = queries.list_user_purchases(user["user_id"])
        return render_template("my_purchases.html", purchases=purchases)
    else:
        return redirect(url_for('login'))

@app.route('/user_page/<username>/products/')
def user_products(username):
    betsy_user = queries.get_user(username)
    if betsy_user:
        user_products = queries.list_user_products(betsy_user['user_id'])
        tag = f"{username}'s products"
        return render_template("products_page.html", tag=tag, products=user_products)
    else:
        abort(404)

@app.route('/products/')
def all_products(): 
    products = queries.get_all_products()
    return render_template("products_page.html", query='All Products', products=products)

@app.route('/products/<tag>')
def search_products_by_tag(tag):
    tagged_products = queries.list_products_per_tag(tag)
    return render_template("products_page.html", query=tag, products=tagged_products)

@app.route('/products/search/')
def search_products():
    query = request.args.get("query")
    products = queries.search(query)
    return render_template("products_page.html", query=query, products=products)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# make a login_required decorator

if __name__ == "__main__":
    app.run(debug=True)