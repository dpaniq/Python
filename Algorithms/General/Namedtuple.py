# ---------------------------------------------------------------------------- #
#                               NamedTuple
# ---------------------------------------------------------------------------- #
from collections import namedtuple

# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks. With namedtuples,
# you don’t have to use integer indices for accessing members of a tuple.
# ------------------------------------------------------------------------------
# Task
# Dr. John Wesley has a spreadsheet
# containing a list of student's ID's, marks, class and name.
#
# Your task is to help Dr. Wesley calculate the average marks of the students.

# !Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written
#     in ANY ORDER in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME.
#  (The spelling and case type of these names won't change.)
#
# Input Format----------------------------------------------------
#
# The first line contains an integer , the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDS, name and class,
#     under their respective column names.
#
# Output Format----------------------------------------------------
# Print the average marks of the list corrected to 2 decimal places.
# ------------------------------------------------------------------------------

z, n, b = 0, int(input()), namedtuple('Avarage', input().split())
print(sum([int(b(*input().split()).MARKS) for i in range(n)])/n)

Car = namedtuple('Car', 'color speed')

z = Car('red', 800).color
print(z)
z = Car('red', 800)
print(z)

# for i in range(n):
#     b(*input().split())
# #     print(d)
# #     z += int(d.MARKS)
# #     print(b.MARKS)
# # print('{:.2f}'.format(z/n))

#     ID         MARKS      NAME       CLASS
#       1          97         Raymond    7
#       2          50         Steven     4
#       3          91         Adrian     9
#       4          72         Stewart    5
#       5          80         Peter      6

# Output 78.00
# -----------------------------------------------
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5

# Output 81.00
# ---------------------------------------------------------------------------- #
#                                 13/02/2019
# ---------------------------------------------------------------------------- #
