from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = 'ケイジ'
    age = 19
    email = 'keiji@example.com'
    return render_template('card.html',
                           username=username,
                           age=age,
                           email=email)

if __name__ == '__main__':
    app.run('0.0.0.0')
