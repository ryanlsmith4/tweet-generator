import sys

def get_word_list(file_name = 'corpus.txt'):
    '''Loads words from a file and cleans text of most special characters'''
    with open(file_name,'r') as f:
        read_words = f.readlines()
        words = []
        for line in read_words:
            split_line = line.strip().split(" ")
            for word in split_line:
                if(word.lower() != ""):
                    words.append(word.lower().strip("(),!."";:,"))
        # print(words)
        return words


if __name__ =='__main__':
    if len(sys.argv) == 2:
        word_list = get_word_list(sys.argv[1])
    else:
         word_list = get_word_list()

    print(word_list)
