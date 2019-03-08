from flask import Flask, jsonify, render_template
from sentence import make_sentence
app = Flask(__name__)

@app.route('/')
def hello_word():
    words = make_sentence()
    return  render_template('index.html', words = words)
