# version 0.2
# ---------------------------------------------------------------------------- #
import re
import enchant  # pip install pyenchant
vocabulary = enchant.Dict("en_US")
from itertools import permutations
from collections import Counter
import random
import time
# ---------------------------------------------------------------------------- #
class Sentence:
    def __init__(self, sentence):            #               User
        self.original = sentence.lower()     # - simple sentence
        self.length = len(sentence.split())  # - number of letter in sentence
        self.text = sentence.split()         # - list of words in sentence
                                             #              Script
        self.check_words = False             # - check status
        self.word_dictionaries = None        # - dictionary of all possible words
        self.create_sentence = None          # - sentences of possible words
        self.all_sent = None                 # - Absolutely all possible sentences
        self.inc_sent = None                 # - ALl incorrect sentences
        self.cor_sent = None                 # - All correct sentences
        self.uniq_sent = None                # - Sorted by uniqueness

    def all_sentence(self):  # ---------------------------------------------- #
        self.created_sentence()
        if self.create_sentence:
            all = []
            for sent in self.create_sentence:
                permut_sentence = list(permutations(sent.split(), self.length))
                for clean_sentence in permut_sentence:
                    all.append(' '.join(clean_sentence))

            self.all_sent = set(all)
            print('\n4. [All_sentence]:', self.all_sent)

    def incorrect_sentence(self):  # ---------------------------------------- #
        ''' Exclude all duplicate words and permutation of original sentence'''
        self.all_sentence()
        if self.all_sent:
            double_words = [single for single in self.all_sent if max(Counter(single.split()).values()) > 1] # Can i do better ?

            orig_perm = [' '.join(x) for x in permutations(self.text, self.length)]
            inc_sent = set(double_words + orig_perm)

            self.inc_sent = sorted(inc_sent)
            print('\n5. [Incorrect_sentence]:', self.inc_sent)

    def correct_sentence(self):  # ------------------------------------------ #
        self.incorrect_sentence()
        if self.inc_sent:
            self.cor_sent = self.all_sent.difference(self.inc_sent)  # <------------------------------------------------------------ Like this Do everywhere! Whiout temporary variable
            print('\n6. [Correct_sentence]:', self.cor_sent)
            # Add uniqueness for each correct sentence
            unique = {}
            for cs in self.cor_sent:
                temp = 0
                for i in range(len(self.original)):
                    if cs[i] != self.original[i]:
                        temp += 1
                unique[cs] = [round(temp* 100 / len(self.original), 1)] # <-----------------------------------------CAN I DO BETTER?
            uniqueness = [[k, unique[k]] for k
                          in sorted(unique, key=unique.get, reverse=True)]
            self.uniq_sent = uniqueness
            print('\n7. [Uniqueness_sentence]:', self.uniq_sent)

# ---------------------------------------------------------------------------- #
class Word(Sentence):
    '''Processing with each word in sentence'''

    def check_word(self):  # ------------------------------------------------- #
        pattern = """[0-9,:;'"\/\\!?~@#$%^&*\(\)\+<>]+"""
        if re.search(pattern, self.original):
            print('Wrong symbols: 123456789,.;:!?...'.center(90))
        else: self.check_words = True
        print('\n1. [Check_word]:', self.check_words)

    def find_real_words(self):  # -------------------------------------------- #
        self.check_word()
        if self.check_words:
            word_dict = {}
            for word in self.text:
                            # <--------union letter and real words! (dobule for!)-------------------------------
                letter = [word for word in permutations(list(word), len(word))]
                real_words = [''.join(real) for real in letter
                                            if vocabulary.check(''.join(real))]
                word_dict[word] = real_words
            self.word_dictionaries = word_dict
            print('\n2. [Find_real_words]:', self.word_dictionaries)

    def created_sentence(self):  # ------------------------------------------- #
        self.find_real_words()
        if self.word_dictionaries:
            # Create a new sentence from find words
            create_sentence = []
            for word in self.word_dictionaries:
                try: # REMOVE and d.get() <----------------------------------------------------------------------------
                    # Result of permutation word have more than two options
                    if len(self.word_dictionaries[word]) >= 2:
                        for var in self.word_dictionaries[word]:
                            sentence_copy = self.original[:]
                            sentence_copy = sentence_copy.replace(word, var)
                            create_sentence.append(sentence_copy)
                except KeyError:
                    pass

            self.create_sentence = create_sentence
            print('\n3. [Created_sentence]:', self.create_sentence)

    def result(self): # ---------------------------------------------------- #
            self.correct_sentence()


# ---------------------------------------------------------------------------- #
#                                   Output
# ---------------------------------------------------------------------------- #
print("word <= 8 letter and sentence < 8 word! a ab abc abcd abcde abcdef abcdefg NOT LONGER!")
example = ['dog is in ocean', 'real swords', 'miss roses act', 'like this', 'dog is god']
while True:
    print('Example: {}'.format(example[random.randint(0, len(example)-1)]))
    trying = Word(input())

    a = time.time() # Start timing
    trying.correct_sentence()
    print(90*'-')
    print(f'Completed in {time.time() - a} seconds\n')  # Stop timing
