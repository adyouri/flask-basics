# -*- coding:utf8 -*-
from flask import Flask, render_template
app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template('index.html', page = u"الصّفحة الرّئيسيّة")


# Hello Page
@app.route("/hello")
def hello():
    return render_template('index.html', page = u"صفحة التّرحيب")


# Posts Page
@app.route("/posts")
def posts():
    posts = [
    u"مُحتوى المقال الأول",
    u"مُحتوى المقال الثاني",
    u"مُحتوى المقال الثالث",
    u"مُحتوى المقال الرابع"
    ]
    return render_template('index.html', posts = posts, page = u"صفحة عرض المقالات")


if __name__ == "__main__":
    app.run(debug=True)
