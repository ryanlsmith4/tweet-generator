import random
import sys



def get_word_list():
    '''
    Retrieve words from a txt file or dictionary
    '''
    word_list = []
    f = open('words.txt', 'r')
    for line in f:
        word_list.append(line.rstrip('\n'))
    # print(word_list)
    return(word_list)


def rearrange(list, number):
    neworder = []
    num = random.sample(list, number)
    neworder.append([num])
    print(*neworder)


if __name__ =='__main__':
    num_words = int(sys.argv[1])
    rearrange(get_word_list(), num_words)
