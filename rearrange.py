import random
import sys
def rearrange():
    words = sys.argv[1:]
    neworder = []
    length=len(words)
    for i in range(length):
       num = random.randint(0, len(words))
       neworder.append(words[num])
       words.pop(num)
    print (*neworder)

if __name__ == '__main__':
    rearrange()
