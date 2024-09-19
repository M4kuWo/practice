from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

categories =[
    {"catid":1,"desc":"meat"},
    {"catid":2,"desc":"dairyyyyyyyyy"},
    {"catid":3,"desc":"bakery"}]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/categories')
def get_categories():
    return categories

@app.route('/dis_cat/<id>')
def dis_cat(id):
    print(id)
    return 'Hello, test!'

@app.route('/test')
def test():
    return 'Hello, test!'


if __name__ == '__main__':
    app.run(debug=True)
