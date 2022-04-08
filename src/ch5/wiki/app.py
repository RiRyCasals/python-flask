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
    return render_template('edit.html',
                           page_name=page_name,
                           body=wikifunc.read_file(page_name))

@app.route('/edit_save/<page_name>', methods=['POST'])
def edit_save(page_name):
    body = request.form.get('body')
    wikifunc.write_file(page_name, body)
    return redirect('/' + page_name)

@app.route('/<page_name>')
def show(page_name):
    print(page_name)
    return render_template('show.html',
                           page_name=page_name,
                           body=wikifunc.read_file(page_name, html=True))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
