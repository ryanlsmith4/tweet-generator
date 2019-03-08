from flask import Flask, jsonify, render_template
from sentence import gen_sentence,
from dictogram import Dictogram
from cleanup import get_word_list



app = Flask(__name__)

@app.route('/')
def hello_word():
    word_list = get_word_list()
    histogram = Dictogram(word_list)
    words = gen_sentence(histogram, word_list)
    return  render_template('index.html', words = words)
