from collections import Counter
import string
def get_word_list():
    '''
    Retrieve words from a txt file or dictionary
    '''
    word_list = []
    new_list = []
    f = open('sherlock.txt').read()
    translator = str.maketrans('', '', string.punctuation)
    f = f.lower()
    wordsFromText = (f.translate(translator)).split()
    for line in wordsFromText:
        word_list.append(line)
        for word in word_list:
            new_list.extend(word.split(' '))
            # dictionary = dict(new_list)
    return(new_list)

def histogram(list):
    '''
    Dictionary function that returns unique values with
    number of reacurrences
    '''
    uni_dict = Counter(list)
    return(uni_dict)

def frequency(word, dictionary):
        print(word, dictionary[word])

def tuple_dict(dictionary):
    tuples_dict = dictionary.items()
    print(tuples_dict)

def lists_of_list(dictionary):
    l_a_l = []
    for item in dictionary:
        # print(item, dictionary[item])
        entry = [item, dictionary[item]]
        l_a_l.append(entry)
        print(l_a_l)






if __name__ =='__main__':
    # frequency('rabbi',histogram(get_word_list()))
    # histogram(get_word_list())
    # tuple_dict(histogram(get_word_list()))
    # lists_of_list(histogram(get_word_list()))
