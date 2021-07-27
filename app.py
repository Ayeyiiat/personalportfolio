from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '51ac8ed6210948128125f8ae2a4ad67f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")









if __name__ == '__main__':
    app.run(debug=True)