from flask import Flask, render_template, redirect, url_for

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template("home_page.html")

@app.route('/home/')
def home():
    return redirect(url_for("frontpage"))

@app.route('/signup/')
def sign_up():
    return render_template("sign_up.html")

@app.route('/about/')
def about():
    return render_template("about.html", page_title='About')

if __name__ == "__main__":
    app.run(debug=True)