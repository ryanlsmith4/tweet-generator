import random

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
                words.append(word.lower().strip("(),!.;"""))
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

def test_sample(list = words):
    temp = []
    freq = {}
    for i in range(0, 10000):
        temp.append(sample(hist))
    for word in temp:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    for key, value in freq.items():
        print(key,format(value/len(temp), '.4f'))

def sample(dict):
    index = random.randint(0, len(dict)-1)
    return dict[index]

if __name__ == '__main__':
    # count = 0
    # for i in range(0, 100):
    #     if i == i:
    #         count += 1
        # print(sample(get_word_list()))
        # print(sample(words))
        # histogram(get_word_list())
        test_sample()
        # test_sample(get_word_list())
        # percent(get_word_list())
        # print(count)
