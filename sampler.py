from histogram import get_word_list, histogram
from histogram import lists_of_list
import random

words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

def test_sample():
    temp_word_list = []
    freq = {}
    manifesto = get_word_list()
    # Uncomment this after testing
    l_o_l_man= lists_of_list(manifesto)

    for i in range(0, 100):
        select_word = sample(l_o_l_man)
        temp_word_list.append(select_word)
    frequency_hist = histogram(temp_word_list)

    print(' '.join(temp_word_list))
    return frequency_hist



    # for word in temp_word_list:
    #     if word not in freq:
    #         freq[word] = 1
    #     else:
    #         freq[word] += 1


def sample(list_of_list):
    ''' Function to take in a list of list and return a random value
        based on weight'''
    # Tokens equals the total number of words
    # Types equals the total number of unique words
    tokens = 0
    cum_prob = 0.0
    for inner_list in list_of_list:
        tokens += inner_list[1]

    # random.uniform returns a float between 0 and .99
    rand_num = random.uniform(0,1)
    for inner_list in list_of_list:
        cum_prob += inner_list[1]/tokens

        if cum_prob >= rand_num:
            # print(inner_list[0])
            # print('Weighted word {}'.format(inner_list[0]))
            return inner_list[0]


if __name__ == '__main__':
    test_sample()
    # lol = lists_of_list(words)
    # print(sample(lol))
