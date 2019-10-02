from flask import Flask, flash, redirect, render_template, request, jsonify, session, abort
import os
import json
from flask_bootstrap import Bootstrap
from conn import get_user, connect, register, up, recent_message, c_up, recent_comment, l_up, delete_c, update_c,\
    d_message, update_m
from message import Message, Comment, Like
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'

Bootstrap(app)
app.secret_key = 'sjdkasf'
UPLOAD_FOLDER = os.path.dirname('static/image/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
def home():
    connect()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        order = 0
        message = recent_message(order)
        cm = recent_comment()
        return render_template('index.html', message=message, comment=cm)


@app.route('/main')
def main_page():
    order = 0
    message = recent_message(order)
    cm = recent_comment()
    return render_template('index.html', message=message, comment=cm)


@app.route('/m_discuss')
def most_d():
    order = 2
    message = recent_message(order)
    cm = recent_comment()
    return render_template('index.html', message=message, comment=cm)


@app.route('/m_like')
def most_l():
    order = 3
    message = recent_message(order)
    cm = recent_comment()
    return render_template('index.html', message=message, comment=cm)

@app.route('/login', methods=['POST'])
def do_admin_login():
    pass_w = request.form['password']
    user_n = request.form['username']
    res = get_user(user_n, pass_w)
    if res == 'welcome':
        session['logged_in'] = True
        session['username'] = request.form['username']
    else:
        flash('wrong password!')
        return render_template('login.html', home="Password Incorrect")
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return home()


@app.route('/regi')
def reg():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def registeration():
    p_w = request.form['pass']
    u_n = request.form['user']
    # ck = check(u_n)
    # if ck == 'found':
    register(u_n, p_w)
    return render_template('login.html')
    # return render_template('register.html', form='User name is in use, get a new one')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    #if request.method == 'POST':
        # check if the post request has the file part
    #if 'file' not in request.files:
        #no = "Please select something. Allowed Format: png, jpg, jpeg, gif."
        #return render_template('index.html', note=no)
    try:
        file = request.files['image']
    except KeyError:
        no = "Please select something. Allowed Format: png, jpg, jpeg, gif."
        return render_template('index.html', note=no)
        # if user does not select file, browser also
        # submit an empty part without filename
    #if file.filename == '':
        #no = "Please select something. Allowed Format: png, jpg, jpeg, gif."
        #return render_template('index.html', note=no)
    msg = request.form['message']
    f_name = datetime.datetime.now().strftime("%m%d%y%H%M") + file.filename
    if file and allowed_file(file.filename):
        message = Message(filepath=f_name, username=session['username'], message=msg)
        up(message)
        f = os.path.join(app.config['UPLOAD_FOLDER'], f_name)
        file.save(f)
        return redirect("#main")
    elif not allowed_file(file.filename):
        no = "Please select something. Allowed Format: png, jpg, jpeg, gif."
        return render_template('index.html', note=no)


@app.route('/comment', methods=['POST'])
def comment():
    # hide the input filepath in html and pass the variable to application
    fn = request.form['filepath']
    msg = request.form['comment']
    cmt = Comment(filename=fn, username=session['username'], comment=msg)
    c_up(cmt)
    return redirect("#main")


@app.route('/like', methods=['POST'])
def like():
    # hide the input filepath in html and pass the variable to application
    fn = request.form['filepath']
    cmt = Like(filename=fn, username=session['username'])
    l_up(cmt)
    return redirect("#main")


@app.route('/del_c', methods=['POST'])
def delete_comment():
    fn = request.form['cnum']
    fn2 = request.form['filepath']
    delete_c(c_num=fn, f_path=fn2)
    return redirect("#main")


@app.route('/c_update', methods=['POST'])
def update_comment():
    fn = request.form['cnum']
    fn2 = request.form['comment']
    update_c(c_num=fn, comment=fn2)
    return redirect("#main")


@app.route('/delete', methods=['POST'])
def delete_m():
    fn = request.form['filepath']
    d_message(file=fn)
    return redirect("#main")


@app.route('/edit_m', methods=['POST'])
def update_message():
    fn = request.form['filename']
    fn2 = request.form['message']
    update_m(message=fn2, file=fn)
    return redirect("#main")


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)
