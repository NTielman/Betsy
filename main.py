import os
from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import verify_password, verify_user
from queries import get_user

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def frontpage(user=False):
    if "user" in session:
        user = session["user"]
    return render_template("home_page.html", user=user)

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

@app.route('/user_profile/')
def user_profile():
    if "user" in session:
        user = session["user"]
        return render_template('user_profile.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/user_profile/add_product/', methods=['GET', 'POST'])
def add_product():
    if "user" in session: #check if user is logged in
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            price = request.form["price"]
            qty = request.form["qty"]
            user = session["user"]

            #try create product
            user_is_valid = verify_user(username, fullname, address, bio, avatar_url, password)
            if user_is_valid:
                user = get_user(username)
                session["user"] = user
                return redirect(url_for("frontpage"))
            else:
                return redirect(url_for('sign_up'))
        else:  #method is GET
            return render_template("add_product.html") #create html and form
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)