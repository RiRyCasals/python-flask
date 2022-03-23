from flask import Flask, request, render_template, redirect, url_for, session

import bbs_login, bbs_data

app = Flask(__name__)
app.secret_key = 'U1sNMeUkZSuuX2Zn'

def show_msg(msg):
    return render_template('msg.html',
                           msg=msg)

@app.route('/')
def index():
    if not bbs_login.is_login():
        return redirect('/login')
    return render_template('index.html',
                           user=bbs_login.get_user(),
                           data=bbs_data.load_data())

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/try_login', methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    print(user, pw)
    if bbs_login.try_login(user, pw):
        return redirect('/')
    return show_msg('ログインに失敗しました')

@app.route('/logout')
def logout():
    bbs_login.try_logout()
    return show_msg('ログアウトしました')

@app.route('/write', methods=['POST'])
def write():
    if not bbs_login.is_login():
        return redirect('/login')
    ta = request.form.get('ta', '')
    if ta == '':
        return show_msg('書込が空でした．')
    bbs_data.save_data_append(user=bbs_login.get_user(),
                              text=ta)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
