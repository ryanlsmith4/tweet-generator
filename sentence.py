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
    return(select_word_hist)

def dict_of_hist(hist, word_list):
    master_dict = {}
    for word in hist:
        entry = dict_of_hist_entry(word, word_list)
        master_dict[word] = entry
    return master_dict

def new_word(word_select, master_hist):
    entry = master_dict[word_select]
    sample = sample_dict(entry)
    return sample

def  make_sentence(word_list, master_hist, sen_length = 10):
    sentence = []
    ran_word = random.randint(0, len(word_list) - 1)
    word_select = word_list[ran_word]
    for i in range(sen_length):
        word = new_word(word_select, master_hist)
        sentence.append(word)
        word_select = word
    print(*sentence)
    return sentence



if __name__ =='__main__':
    if len(sys.argv) == 2:
        word_list = get_word_list(sys.argv[1])
    else:
        word_list = get_word_list()
    histogram = Dictogram(word_list)
    master_dict = dict_of_hist(histogram, word_list)
    # var = dict_of_hist_entry('fish', word_list)
    # print(master_dict)
    make_sentence(word_list, master_dict, 20)
