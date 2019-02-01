
# The last contained: 300 lines. Сontains 115 now. Gromov Bogdan
# ---------------------------------------------------------------------------- #
import re
import enchant  # pip install pyenchant
vocabulary = enchant.Dict("en_US")
from itertools import permutations
from collections import Counter
import time
# ---------------------------------------------------------------------------- #
class Sentence:
    def __init__(self, sentence):            # User ---------------------------#
        self.original = sentence             # - simple sentence
        self.length = len(sentence.split())  # - number of letter in sentence
                                             # Script ------------------------ #
        self._text = sentence.split()        # - list of words in sentence
        self._check_words = False            # - check status
        self._word_dictionaries = None       # - dictionary of all possible words
        self._create_sentence = None         # - sentences of possible words
        self._all_sent = None                # - Absolutely all possible sentences
        self._inc_sent = None                # - ALl incorrect sentences
        self._cor_sent = None                # - All correct sentences with uniqueness

    def _all_sentence(self):  # ---------------------------------------------- #
        all = []
        for sent in self._create_sentence:
            permut_sentence = list(permutations(sent.split(), self.length))
            for clean_sentence in permut_sentence:
                all.append(' '.join(clean_sentence))

        self._all_sent = set(all)
        return sorted(set(all))

    def _incorrect_sentence(self):  # ---------------------------------------- #
        # Exclude all duplicate words
        double_words = [single for single in self._all_sent
                               if max(Counter(single.split()).values()) > 1]
        # Exclude all permutation of original sentence
        orig_perm = [' '.join(x) for x in permutations(self._text, self.length)]
        inc_sent = set(double_words + orig_perm)

        self._inc_sent = inc_sent
        return sorted(inc_sent)

    def _correct_sentence(self):  # ------------------------------------------ #
        cor_sent = self._all_sent.difference(self._inc_sent)

        # Add uniqueness for each correct sentence
        unique = {}
        for cs in cor_sent:
            temp = 0
            for i in range(len(self.original)):
                if cs[i] != self.original[i]:
                    temp += 1
            unique[cs] = [round(temp* 100 / len(self.original), 1)]
        uniqueness = [[k, unique[k]] for k
                      in sorted(unique, key=unique.get, reverse=True)]
        return uniqueness

# ---------------------------------------------------------------------------- #
class Word(Sentence):
    '''Processing with each word in sentence'''

    def check_word(self):  # ------------------------------------------------- #
        pattern = '[A-Z\0-9]'
        if not [False for words in self._text if re.search(pattern, words)]:
            self._check_words = True
            return True

    def find_real_words(self):  # -------------------------------------------- #
        if self.check_word():
            word_dict = {}
            for word in self._text:
                letter = [word for word in permutations(list(word), len(word))]
                real_words = [''.join(real) for real in letter
                                            if vocabulary.check(''.join(real))]
                word_dict[word] = real_words
            return word_dict

    def created_sentence(self):  # ------------------------------------------- #
        self._word_dictionaries = self.find_real_words()

        # Create a new sentence from find words
        create_sentence = []
        for word in self._word_dictionaries:
            try:
                # Result of permutation word have more than two options
                if len(self._word_dictionaries[word]) >= 2:
                    for var in self._word_dictionaries[word]:
                        sentence_copy = self.original[:]
                        sentence_copy = sentence_copy.replace(word, var)
                        create_sentence.append(sentence_copy)
            except KeyError:
                pass

        self._create_sentence = create_sentence
        return create_sentence

    def __result(self): # ---------------------------------------------------- #
        a = time.time()
        step1 = self.check_word()
        step2 = self.find_real_words()
        step3 = self.created_sentence()
        step4 = self._all_sentence()
        step5 = self._incorrect_sentence()
        step6 = self._correct_sentence()
        b = time.time() - a
        print(*[wu for wu in step6], f'Completed in {b} seconds', sep = '\n')

    def get(self):
        self.__result()
# ---------------------------------------------------------------------------- #
while True:
    trying = Word(input())
    trying.get()
    print("X"*30)