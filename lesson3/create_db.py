# -*- coding: utf-8 -*-
import sqlite3

# الاتّصال بقاعدة البيانات
db = sqlite3.connect('database.db')


# إنشاء مُؤشّر في قاعدة البيانات لنتمكّن من تنفيذ استعلامات SQL
cursor = db.cursor()

# إنشاء الجدول
cursor.execute("""
    CREATE TABLE posts(
        id INTEGER PRIMARY KEY,
        title TEXT, 
        content TEXT
        )""")
# إدخال القيم إلى الجدول


cursor.execute('''INSERT INTO posts(title, content)
                      VALUES(?,?)''',
           (u'عنوان المقال الأول',
            u'محتوى المقال الأول'))

cursor.execute('''INSERT INTO posts(title, content)
                  VALUES (?,?)''', 
            (u'عنوان المقال الثّاني',
             u'مُحتوى المقال الثّاني'))
 # تطبيق التّغييرات
db.commit()
