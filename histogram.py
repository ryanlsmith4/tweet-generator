from collections import Counter
import string

words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


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

def frequency(choice):
    count = 0
    for word in get_word_list():
        if word == choice:
            count += 1
    print(count)
    return(count)

def count(list):
    count = 0
    for word in list:
        if word == word:
            count += 1
    print(count)
    return(count)

def list_of_tuples(list):
    l_t = []
    inner_tuple = ()
    for word in list:
        found = False
        for inner_tuple in l_t:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                l_t.remove(inner_tuple)
                l_t.append((word, count))
                found = True
                break
        if not found:
            l_t.append(((word, 1)))
    return(l_t)
    print(l_t)


def lists_of_list(list):
    l_o_l = []
    inner_list = []
    for word in list:
        found = False
        for inner_list in l_o_l:
            if word == inner_list[0]:
                found = True
                inner_list[1] += 1
                break
        if not found:
            l_o_l.append([word, 1])
    return(l_o_l)







if __name__ =='__main__':
    # print(get_word_list())
    # frequency('a')
    # histogram(get_word_list())
    # list_of_tuples(words)
    lists_of_list(words)
