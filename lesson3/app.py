# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, url_for, request
import manage_db

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    posts = manage_db.get_posts()
    return render_template('index.html', posts = posts)


# Create Post Page
@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        manage_db.create(title, content)
    return redirect(url_for('home'))


# Single Post Page
@app.route("/post/<post_id>")
def post(post_id):
    post = manage_db.get_post_by_id(post_id)
    return render_template('post.html', post = post)


# Delete Post 
@app.route("/delete/<post_id>")
def delete(post_id):
    manage_db.delete(post_id)
    return redirect(url_for('home')) 


if __name__ == "__main__":
    app.run(debug=True)
