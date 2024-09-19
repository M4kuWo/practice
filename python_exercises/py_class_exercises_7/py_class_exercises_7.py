from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

array =[]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test1')
def test1():
    return 'Hello, test1!'

@app.route('/test2')
def test2():
    return 'Hello, test2!'

@app.route('/test3')
def test3():
    return 'Hello, test3!'


if __name__ == '__main__':
    app.run(debug=True)
