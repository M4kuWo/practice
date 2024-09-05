from flask import Flask, render_template

app = Flask(__name__)

ar = []

data = []

# Define a basic route
@app.route('/watermelon')
def watermelonPage():
    return render_template('watermelon.html')

@app.route('/monkey')
def MonkeyPage():
    return render_template('groovy_monkey.html')

@app.route('/cat')
def CatPage():
    return render_template('wtf_cat.html')

@app.route('/placeholder')
def placeHolder():
    return "testiiiiing!"


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
