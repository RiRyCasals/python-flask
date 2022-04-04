import os
import json
import sqlite3
from flask import Flask, request

bash_path = os.path.dirname(__file__)
db_path = bash_path + '/zip.sqlite'
form_path = bash_path + '/zip-form.html'

app = Flask(__name__)

@app.route('/')
def index():
    with open(form_path) as f:
        return f.read()

@app.route('/api')
def api():
    q = request.args.get('q', '')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT ken,shi,cho FROM zip WHERE code=?', [q])
    items = c.fetchall()
    conn.close()
    res = []
    for r in items:
        ken, shi, cho = (r[0], r[1], r[2])
        res.append(ken + shi + cho)
        print(q, ': ', ken + shi + cho)
    return json.dumps(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
