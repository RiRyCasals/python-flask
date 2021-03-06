from flask import Flask, request, redirect, render_template
import wikifunc

app = Flask(__name__)

@app.route('/')
def index():
    return show('FrontPage')

@app.route('/new')
def new_page():
    page_name = request.args.get('page_name')
    if page_name is None:
        return render_template('new.html')
    else:
        return redirect('/edit/' + page_name)

@app.route('/edit/<page_name>')
def edit(page_name):
    body, hash = wikifunc.read_file(page_name)
    return render_template('edit.html',
                           page_name=page_name,
                           body=body,
                           hash=hash,
                           warn='')

@app.route('/edit_save/<page_name>', methods=['POST'])
def edit_save(page_name):
    body2 = request.form.get('body')
    hash2 = request.form.get('hash')
    _, hash1 = wikifunc.read_file(page_name)
    if hash1 != hash2:
        print('diff=', hash1, hash2)
        res = wikifunc.get_diff(page_name, body2, hash2)
        return render_template('edit.html',
                               page_name=page_name,
                               body=res,
                               hash=hash1,
                               warn='編集に競合がありました')
    wikifunc.write_file(page_name, body2)
    return redirect('/' + page_name)

@app.route('/<page_name>')
def show(page_name):
    body, _ = wikifunc.read_file(page_name, html=True)
    return render_template('show.html',
                           page_name=page_name,
                           body=body)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
