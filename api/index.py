from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, opik!'

@app.route('/about')
def about():
    return 'About'

@app.route('/ucok')
def ucok():
    return 'ucok'