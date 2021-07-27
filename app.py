from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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