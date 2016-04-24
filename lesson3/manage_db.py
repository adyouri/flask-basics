import sqlite3
def create(title, content):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO posts(title, content)
                      VALUES(?,?)''', (title, content))
    db.commit()


def get_posts():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    query = cursor.execute('''SELECT * FROM posts''')
    posts = query.fetchall()
    return posts


def get_post_by_id(post_id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    post_id = int(post_id)
    query = cursor.execute('''SELECT title, content
                              FROM posts 
                              WHERE id=?''',(post_id,))
    post = query.fetchone()
    return post


def delete(post_id):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM posts WHERE id=?''',
            (post_id,))
    db.commit()
