from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'I am home'


@app.route('/about/')
def about():
    return 'This is a Flask website'


@app.route('/hello/<name>/')
def hello(name):
    return 'Hello {}'.format(name)


@app.route('/add/<num_1>/<num_2>/')
def add(num_1, num_2):
    result = int(num_1) + int(num_2)
    return str(result)


app.run(debug=True)
