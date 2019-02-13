# ---------------------------------------------------------------------------- #
#                               Insertion Sort
# ---------------------------------------------------------------------------- #

import re

# 1. Positive / negative float numbers
# ---------------------------------------------------------------------------- #
# pattern = '^[+-]?[0-9]*?\.[0-9]*$'
# for i in range(int(input())):
#     print(True if re.match(pattern, input()) else False)


# 2. Regex split
# ---------------------------------------------------------------------------- #
# You are given a string 'String' consisting only of:
#         0-9 digits, ',' commas  and '.' dots .

# Your task is to complete the regex_pattern defined below, which will be used to
# re.split() all of the , and . symbols in . It’s guaranteed that every comma and
# every dot in 'String' is preceeded and followed by a digit.

# ------------- Code --------------
# pattern = '[*,.]'
# print(*[i for i in re.split(pattern, input())], sep='\n')


# 3. Repeated alphanumeric character
# ---------------------------------------------------------------------------- #
# You are given a string .
# Your task is to find the first occurrence of an alphanumeric character in
# 'String'(read from left to right) that has consecutive repetitions.

# Input Format
# A single line of input containing the string 'String'.
# '..12345678910111213141516171820212223'

# Output Format
# 1
# Explanation
# .. is the first repeating character, but it is not alphanumeric.
# 1 is the first (from left to right) alphanumeric repeating character of the
# string in the substring 111 - 1 is repeated.
# Print the first occurrence of the repeating character.
# If there are no repeating characters, print -1.

# ------------- Code --------------
# m = re.search(r'(\w)\1+', input())
# print(m.group(0) if m else -1)

# ---------------------------------------------------------------------------- #
#                                 13/02/2019
# ---------------------------------------------------------------------------- #
