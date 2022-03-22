import os
from flask import Flask, request, redirect

DATAFILE = './board-data.txt'

app = Flask(__name__)

@app.route('/')
def index():
    msg = 'まだ書込はありません．'
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()
    return """
        <html>
            <body>
                <h1>メッセージボード</h1>
                <div style="background-color: yellow; padding: 3em;">
                    {0}
                </div>
                <h3>ボードの内容を更新：</h3>
                <form action="/write" method="POST">
                    <textarea name="msg" rows="6" cols="60"></textarea>
                    <br/>
                    <input type=submit value="書込">
                </form>
            </body>
        </html>
    """.format(msg)

@app.route('/write', methods=['POST'])
def write():
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
