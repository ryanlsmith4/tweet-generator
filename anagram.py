import nltk
all_words = nltk.corpus.words.words()

jumbled_letters = "ryansmith"
anagram_results = []

len_full_phrase = len(jumbled_letters)

letter_distribution = nltk.FreqDist(jumbled_letters)
trimmed_lowercase_wordlist = [w.lower() for w in all_words if len(w) <= len_full_phrase]
matching_wordlist = [w for w in trimmed_lowercase_wordlist if nltk.FreqDist(w) <= letter_distribution]
sorted_wordlist = sorted(matching_wordlist, key = lambda s: len(s) * -1 )
len_wordlist = len(sorted_wordlist)
#for faster runtime we move these out of the while loops
nospace = "".join
distribution = nltk.FreqDist
#
i_first_word = 0
while i_first_word < len_wordlist:
    first_word = sorted_wordlist[i_first_word]
    len_first_word = len(first_word)
    remaining_letters = list(jumbled_letters)
    if len_first_word == len_full_phrase:
        sentence = [first_word, "", ""]
        anagram_results.append(sentence)
        print("anagram found: {}", sentence)
    elif len_first_word < len_full_phrase:
        #strip the matching word from the remaining letters
        first_word_chars = list(first_word)
        for char in first_word_chars:
            remaining_letters.remove(char)
        i_second_word = i_first_word
        while i_second_word < len_wordlist:
            second_word = sorted_wordlist[i_second_word]
            len_second_word = len(second_word)
            if len_second_word + len_first_word == len_full_phrase:
                sentence = [first_word, second_word, ""]
                if distribution(nospace(sentence)) == letter_distribution:
                    anagram_results.append(sentence)
                    print("anagram found: {}", sentence)
            elif len_second_word + len_first_word < len_full_phrase and nltk.FreqDist(second_word) <= nltk.FreqDist(remaining_letters):
                #strip the matching word from the remaining letters
                second_word_chars = list(second_word)
                for char in second_word_chars:
                    remaining_letters.remove(char)
                i_third_word = i_second_word
                while i_third_word < len_wordlist:
                    third_word = sorted_wordlist[i_third_word]
                    len_third_word = len(third_word)
                    if len_first_word + len_second_word + len_third_word == len_full_phrase:
                        sentence = [first_word, second_word, third_word]
                        if distribution(nospace(sentence)) == letter_distribution:
                            anagram_results.append(sentence)
                            print("anagram found: {}", sentence)
                    #only go up to three words in the anagram
                    i_third_word += 1
            i_second_word += 1
    i_first_word += 1
#
# write anagram results to file
#
filename = jumbled_letters+'_anagrams.csv'
anagram_results_file = open(filename, 'w')
for anagram in anagram_results:
    line = ','.join(anagram)
    anagram_results_file.write("\n"+line)

#anagram python script I followed andrew tremblay tutorial!!
#http://www.andrew-tremblay.com/blog/anagrams-python-nltk-001/
