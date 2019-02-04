from collections import Counter
import string

def get_word_list(file_name = 'this.txt'):
    '''Loads words from a file and cleans text of most special characters'''
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    words = list()
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.lower().strip("(),!."""))
    # print(words)

    return words

def histogram(list):
    '''
    Dictionary function that returns unique values with
    number of reacurrences
    '''
    dict = {}
    for word in list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    # print(dict)
    return(dict)

def frequency(word, dictionary):
        print(word, dictionary[word])

def tuple_dict(dictionary):
    tup_list = []
    for item in dictionary:
        entry = (item, dictionary[item])
        tup_list.append(entry)
    print(tup_list)

def lists_of_list(dictionary):
    l_a_l = []
    for item in dictionary:
        # print(item, dictionary[item])
        entry = [item, dictionary[item]]
        l_a_l.append(entry)
    print(l_a_l)






if __name__ =='__main__':
    # get_word_list()
    frequency('crime',histogram(get_word_list()))
    # histogram(get_word_list())
    # tuple_dict(histogram(get_word_list()))
    # lists_of_list(histogram(get_word_list()))
