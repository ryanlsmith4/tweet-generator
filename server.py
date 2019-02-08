from flask import Flask, jsonify, render_template
from sampler import test_sample
app = Flask(__name__)

@app.route('/')
def hello_word():
    words = test_sample()
    return  render_template('index.html', words = words)
