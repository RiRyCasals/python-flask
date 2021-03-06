import os
import math
from flask import Flask, request

limit = 3
data = [
    {"name": "リンゴ", "price": 370},
    {"name": "イチゴ", "price": 660},
    {"name": "バナナ", "price": 180},
    {"name": "マンゴ", "price": 450},
    {"name": "トマト", "price": 250},
    {"name": "セロリ", "price": 180},
    {"name": "パセリ", "price": 220},
    {"name": "ミカン", "price": 550},
    {"name": "エノキ", "price": 340},
]

app = Flask(__name__)

@app.route('/')
def index():
    page_s = request.args.get('page', '0')
    page = int(page_s)
    index = page * limit
    s = '<div>'
    for i in data[index: index+limit]:
        s += '<div class="item">'
        s += '品目： ' + i['name'] + '<br>'
        s += '値段： ' + str(i['price']) + '円'
        s += '</div>'
    s += '</div>'
    s += make_pager(page, len(data), limit)
    return '''
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://unpkg.com/purecss@2.1.0/build/pure-min.css" integrity="sha384-yHIFVG6ClnONEA5yB5DJXfW2/KC173DIQrYoZMEtBvGzmf0PKiGyNEqe9N6BNDBH" crossorigin="anonymous">
                <style>
                    .item {
                        border: 1px solid silver;
                        background-color: #f0f0ff;
                        padding: 9px;
                        margin: 15px;
                    }
                </style>
            </head>
            <body>
                <h1 style="text-align:center;">商品</h1>
    ''' + s + '''
            </body>
        </html>
    '''

def make_button(href, label):
    klass = 'pure-button'
    if href == '#':
        klass += ' pure-button-disabled'
    return '''
        <a href="{0}" class="{1}">{2}</a>
    '''.format(href, klass, label)

def make_pager(page, total, per_page):
    page_count = math.ceil(total / per_page)
    s = '<div style="text-align:center;">'
    prev_link = '?page=' + str(page - 1)
    if page <= 0:
        prev_link = '#'
    s += make_button(prev_link, '←前へ')
    s += '{0}/{1}'.format(page+1, page_count)
    next_link = '?page=' + str(page + 1)
    if page_count-1 <= page:
        next_link = '#'
    s += make_button(next_link, '次へ→')
    s += '</div>'
    return s

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
