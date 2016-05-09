# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, url_for, request, session, flash
import manage_db
from functools import wraps


def require_login(function):
    @wraps(function) 
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            flash(u'سجّل دخولك أولا')
            return redirect(url_for('home'))
    return wrapper


app = Flask(__name__)
app.config.from_object('config')


# Home Page
@app.route("/")
def home():
    posts = manage_db.get_posts()
    return render_template('index.html', posts = posts)


# Create Post Page
@app.route("/create", methods=['GET', 'POST'])
@require_login
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        manage_db.create(title, content)
        flash(u'أضيف المقال بنجاح!')
    return redirect(url_for('home'))


# Single Post Page
@app.route("/post/<post_id>")
def post(post_id):
    post = manage_db.get_post_by_id(post_id)
    return render_template('post.html', post = post)


# Delete Post 
@app.route("/delete/<post_id>")
@require_login
def delete(post_id):
    manage_db.delete(post_id)
    flash(u'حُذف المقال بنجاح!')
    return redirect(url_for('home')) 


# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == app.config['USERNAME'] and password == app.config['PASSWORD']:
            session['logged_in'] = True
            flash(u'سُجّل دخولك بنجاح!')
        else:
            return redirect(url_for('home'))
    return redirect(url_for('home'))


# Logout Route
@app.route("/logout")
@require_login
def logout():
    session.pop('logged_in', None)
    flash(u'سُجّل خروجك بنجاح!')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
