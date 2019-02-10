# ---------------------------------------------------------------------------- #
#                                      1
# ---------------------------------------------------------------------------- #

dictionary = {input('Word to dict: ').lower() for i in range(int(input('How many words: ')))}
sentences =  {_ for i in range(int(input('How many sentences: '))) for _ in input(f'{i} string is: ').split()}
print(*[w for w in sentences if w.lower() not in dictionary], '- were NOT in the dictionary')
# ---------------------------------------------------------------------------- #
#                                      1
# ---------------------------------------------------------------------------- #
