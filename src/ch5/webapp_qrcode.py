import os
import qrcode
from tinydb import TinyDB
from flask import Flask, request, redirect

JUMP_URL = 'https://kujirahand.com'
FILE_COUNTER = os.path.dirname(__file__) + '/counter.json'

app = Flask(__name__)
db = TinyDB(FILE_COUNTER)

def get_counter():
    table = db.table('count_visitor')
    a = table.all()
    if len(a) == 0:
        table.insert({'v': 0})
        return 0
    return a[0]['v']

@app.route('/')
def index():
    url = request.host_url + 'jump'
    img = qrcode.make(url)
    img.save(os.path.dirname(__file__) + '/static/qrcode_jump.png')
    counter = get_counter()
    return '''
        <h1>以下のQRコードを名刺に印刷</h1>
        <img src="static/qrcode_jump.png" width="300"><br>{0}<br>
        現在の訪問者は，{1}人です．
    '''.format(url, counter)

@app.route('/jump')
def jump():
    v = get_counter()
    table = db.table('count_visitor')
    table.update({'v': v + 1})
    return redirect(JUMP_URL)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
