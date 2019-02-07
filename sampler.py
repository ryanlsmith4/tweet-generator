from histogram import get_word_list
from histogram import lists_of_list
import random

words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

def test_sample():
    temp = []
    freq = {}
    manifesto = get_word_list()
    lol = lists_of_list(manifesto)

    for i in range(0, 1000):
        temp.append(sample(lol))

    for word in temp:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    for key, value in freq.items():
        print(key,format(value/len(temp), '.4f'))

def sample(list_of_list):
    weight = 0
    cum_prob = 0.0
    for word_count in list_of_list:
        weight += word_count[1]

    rand_num = random.uniform(0,1)
    for word_count in list_of_list:
        cum_prob += word_count[1]/weight
        if cum_prob >= rand_num:
            # print(word_count[0])
            return word_count[0]


if __name__ == '__main__':
    test_sample()
