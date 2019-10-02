import sys
import os
import sqlite3 as sql
from contextlib import closing
import datetime
from message import Message, Comment

conn = None

# https://bootsnipp.com/snippets/featured/pinterest-like-responsive-grid


def connect():
    global conn
    if not conn:
        DB_FILE = "static/my_database.sqlite"
        conn = sql.connect(DB_FILE, check_same_thread=False)
        conn.row_factory = sql.Row


def get_user(user_n, pass_w):
    query = '''SELECT username, password
               FROM users
               WHERE username = ? and password = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user_n, pass_w))
        results = c.fetchall()
    if results:
        return "welcome"
    else:
        return None


def check(u_n):
    query = '''SELECT username
               FROM users
               WHERE username = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (u_n,))
        results = c.fetchall()
    if results:
        return "found"
    else:
        return "not found"


def register(u_n, p_w):
    query = '''INSERT INTO users (username, password) 
             VALUES (?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (u_n, p_w))
        conn.commit()


def up(message):
    message.time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
    qy = '''INSERT INTO mesg (username, filepath, time, message) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(qy, (message.username, message.filepath, message.time, message.message))
        conn.commit()


def make_message(row):
    return Message(row['username'], row['filepath'], row['message'], row['time'], row['likenumber'], row['m_num'],
                   row['c_number'], row['up_ed'])


def recent_message(order):
    # add_like()
    query = '''SELECT * FROM mesg ORDER BY time DESC'''
    query2 = '''SELECT * FROM mesg ORDER BY c_number DESC'''
    query3 = '''SELECT * FROM mesg ORDER BY likenumber DESC'''
    with closing(conn.cursor()) as c:
        if order == 2:
            c.execute(query2)
        elif order == 3:
            c.execute(query3)
        else:
            c.execute(query)
        results = c.fetchall()
    message = []
    for row in results:
        message.append(make_message(row))
    return message


def c_up(comment):
    comment.time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
    qy = '''INSERT INTO comment (filename, username, comment, time) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(qy, (comment.filename, comment.username, comment.comment, comment.time))
        conn.commit()
    sql1 = '''SELECT filename
               FROM comment WHERE filename = ?'''
    with closing(conn.cursor()) as t:
        t.execute(sql1, (comment.filename,))
        results = t.fetchall()
    c_n = 0
    if results:
        c_n = len(results)
    query2 = '''UPDATE mesg SET c_number = ? WHERE m_num = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (c_n, comment.filename))
        conn.commit()
    return


def make_comment(row):
    return Comment(row['filename'], row['username'], row['comment'], row['time'], row['c_num'], row['up_ed'])


def recent_comment():
    query = '''SELECT * FROM comment ORDER BY time DESC'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    comment = []
    for row in results:
        comment.append(make_comment(row))
    return comment


def l_up(cmt):
    query = '''SELECT username, filename
               FROM lk_t
               WHERE username = ? and filename = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (cmt.username, cmt.filename))
        results = c.fetchall()
    if results:
        return "You can't like it more than once bro"
    else:
        qy = '''INSERT INTO lk_t (filename, username) 
            VALUES (?, ?)'''
        with closing(conn.cursor()) as t:
            t.execute(qy, (cmt.filename, cmt.username))
            conn.commit()
        return update_l(cmt=cmt.filename)


def update_l(cmt):
    sql1 = '''SELECT filename
               FROM lk_t WHERE filename = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql1, (cmt,))
        results = c.fetchall()
    lk_n = 0
    if results:
        lk_n = len(results)
    query2 = '''UPDATE mesg SET likenumber = ? WHERE m_num = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (lk_n, cmt))
        conn.commit()
    return


def update_c(c_num, comment):
    u_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
    query2 = '''UPDATE comment SET comment = ?, up_ed = ? WHERE c_num = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (comment, u_time, c_num))
        conn.commit()
    return


def update_m(message, file):
    u_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
    query2 = '''UPDATE mesg SET message = ?, up_ed = ? WHERE m_num = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (message, u_time, file))
        conn.commit()
    return


def delete_c(c_num, f_path):
    sql1 = '''DELETE FROM comment
            WHERE c_num = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql1, (c_num,))
        conn.commit()
    sql1 = '''SELECT filename
               FROM comment WHERE filename = ?'''
    with closing(conn.cursor()) as t:
        t.execute(sql1, (f_path,))
        results = t.fetchall()
    c_n = 0
    if results:
        c_n = len(results)
    query2 = '''UPDATE mesg SET c_number = ? WHERE m_num = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (c_n, f_path))
        conn.commit()
    return

def d_message(file):
    sql1 = '''DELETE FROM mesg
            WHERE m_num = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql1, (file,))
        conn.commit()
    sql1 = '''DELETE FROM comment
            WHERE filename = ?'''
    with closing(conn.cursor()) as t:
        t.execute(sql1, (file,))
        conn.commit()
    query2 = '''DELETE FROM lk_t
            WHERE filename = ?'''
    with closing(conn.cursor()) as b:
        b.execute(query2, (file,))
        conn.commit()
    return


def close():
    if conn:
        conn.close()
