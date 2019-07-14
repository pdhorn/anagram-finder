# import sys
# sys.setrecursionlimit(4000)

from collections import Counter
from copy import deepcopy

with open('/usr/share/dict/words', 'r') as file:
    words = file.readlines()
    words = [word.strip('\n').lower() for word in words]
    words = list(filter(lambda x: len(x) > 2, words))

word_dict = {word:1 for word in words}

subs = {}
for word in words:
    for ind in range(1,len(word)+1):
        subs[word[:ind]] = 1

class anagram_finder():
    def __init__(self, seed):
        self.seed = seed
    
    def calculate(self):
        seed = self.seed

        if len(seed) > 10:
            raise Exception("Input is too long.")

        seed_counter = Counter(seed)

        anagrams = {}

        nexts = []
        for ind in range(len(seed)):
            ltr, tmp =  seed[ind], dict(Counter(seed[:ind]+seed[ind+1:]))
            nexts.append((ltr, tmp))
            if word_dict.get(ltr):
                anagrams[ltr] = 1

        while len(nexts) > 0:
            new_nexts = []

            for item in nexts:
                for next_letter in item[1].keys():
                    next_stem = item[0]+next_letter
                    if subs.get(next_stem):
                        if word_dict.get(next_stem):
                            anagrams[next_stem] = 1
                        new_dict = deepcopy(item[1])
                        new_dict[next_letter] = new_dict[next_letter] - 1
                        if new_dict[next_letter] == 0:
                            del new_dict[next_letter]
                        new_nexts.append((next_stem, new_dict))
            nexts = new_nexts

        anagrams = list(anagrams.keys())

        anagrams.sort(key=lambda item: (len(item), item))

        return(anagrams)
