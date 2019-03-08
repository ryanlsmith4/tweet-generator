import sys
import random
from dictogram import Dictogram
from cleanup import get_word_list
from sampler import sample_dict

def dict_of_hist_entry(select_word, word_list):
    words_after_list = []
    for index in range(len(word_list) -1):
        if select_word == word_list[index]:
            words_after_list.append(word_list[index + 1])
    select_word_hist = Dictogram(words_after_list)
    # print(select_word_hist)
    return(select_word_hist)

def gen_sentence(hist, word_list): #ATTENTION GRADER THIS FX GENS THE 1st ORDER MARKOV
    new_sentence = []
    if len(new_sentence) == 0:
        sample = sample_dict(hist)
        new_sentence.append(sample)
    # master_dict = {}
    # for word in hist:
    while len(new_sentence) < 15:

        entry = dict_of_hist_entry(sample, word_list)
        sample = sample_dict(entry)
        new_sentence.append(sample)

        # master_dict[word] = entry
    new_sentence[len(new_sentence) -1] = '.'
    better_sentence = ' '.join(new_sentence)
    print(better_sentence)
    return better_sentence

if __name__ =='__main__':
    # if len(sys.argv) == 2:
    #     word_list = get_word_list(sys.argv[1])
    # else:
    word_list = get_word_list()
    histogram = Dictogram(word_list)
    # master_dict = dict_of_hist(histogram, word_list)
    # # var = dict_of_hist_entry('fish', word_list)
    gen_sentence(histogram, word_list)
    # print(master_dict)
    # make_sentence(word_list, master_dict)
    # dict_of_hist_entry('king', word_list)
