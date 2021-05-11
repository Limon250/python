from flask import Flask, url_for
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1>Hello, World!</h1>'
app.add_url_rule('/', 'index', hello)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

if __name__ == "__main__":
    app.run()