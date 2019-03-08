from flask import Flask, jsonify, render_template
from sentence import gen_sentence
app = Flask(__name__)

@app.route('/')
def hello_word():
    words = gen_sentence()
    return  render_template('index.html', words = words)
