# Lets break it down.
#
# A simple list-comprehension:
#
# [x for x in collection]
# This is easy to understand if we break it into parts: [A for B in C]
# --- A is the item that will be in the resulting list
# --- B is each item in the collection C
# --- C is the collection itself.

# In this way, one could write:
#
# [x.lower() for x in words]
# In order to convert all words in a list to lowercase.
#
# It is when we complicate this with another list like so:
#
# [x for y in collection for x in y] # [A for B in C for D in E]
# Here, something special happens. We want our final list to include A items, and A items are found inside B items, so we have to tell the list-comprehension that.
#
# A is the item that will be in the resulting list
# B is each item in the collection C
# C is the collection itself
# D is each item in the collection E (in this case, also A)
# E is another collection (in this case, B)
# This logic is similar to the normal for loop:
#
# for y in collection:     #      for B in C:
#     for x in y:          #          for D in E: (in this case: for A in B)
#         # receive x      #              # receive A
# To expand on this, and give a great example + explanation, imagine that there is a train.
#
# The train engine (the front) is always going to be there (the result of the list-comprehension)
#
# Then, there are any number of train cars, each train car is in the form: for x in y
#
# A list comprehension could look like this:
#
# [z for b in a for c in b for d in c ... for z in y]
# Which would be like having this regular for-loop:
#
# for b in a:
#     for c in b:
#         for d in c:
#             ...
#                 for z in y:
#                     # have z
# In other words, instead of going down a line and indenting, in a list-comprehension you just add the next loop on to the end.

# [x for       x         in b] - single for
# [x for |b in a | for x in b] - double for

print(*[x for x in range(7)], sep = (' '))

# 1. Выводим X
# 2. Для каждого Y в итераторе
# 3. Для каждого X в Y
# [x for y in collection for x in y]

# print(*[x for n in range(7) for x in range(n)], sep = ' ')

# this code
for i in range(7):
    for j in range(i):
        print(i)

# its similar:
print(*[n for n in range(int(intput())) for x in range(n)], sep = ' ')
