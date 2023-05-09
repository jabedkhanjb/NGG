from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    number = int(request.form['number'])
    guess = int(request.form['guess'])

    if guess == number:
        message = 'You win!'
    elif guess < number:
        message = 'Too low, try again!'
    else:
        message = 'Too high, try again!'

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
