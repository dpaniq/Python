# ---------------------------------------------------------------------------- #
#                                    Zip
# ---------------------------------------------------------------------------- #
print(list(zip([2,1], [3,2])))

em = []
n, x = map(int, input().split())

z = zip(*[list(map(float,input().split())) for i in range(x)])
print(z)
print(*[sum(i)/x for i in z], sep='\n')
# for i in range(x):
#     em.append(list(map(float,input().split())))
# #
# print(em)
# z = list(zip(*em))
# print(z)
#
# for i in z:
#     print(i)
#     print(sum(i)/x)
#     print()
# ---------------------------------------------------------------------------- #
#                                   13/02/2019
# ---------------------------------------------------------------------------- #
