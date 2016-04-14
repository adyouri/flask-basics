# -*- coding:utf8 -*-
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
    page = 'Home Page'
    return page


@app.route("/hello")
def hello():
    return u"""
    <h1 style="direction:rtl">
    السّلام عليكم ورحمة الله وبركاته
    </h1>
    """


@app.route("/say_hello/<name>")
def say_hello(name):
    return u"Hello {}".format(name)


@app.route("/first_last")
def first_last():
    first_name = request.args.get('first_name').capitalize()
    last_name = request.args.get('last_name').upper()
    return "<h3>First Name: {} <br>Last Name: {}</h3>".format(first_name, last_name)


if __name__ == "__main__":
    app.run(debug=True)

