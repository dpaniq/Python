# ---------------------------------------------------------------------------- #
#                             Fibonacci Sequence
# ---------------------------------------------------------------------------- #

# My simple option with limited output
# def F(n):
#      # return a list of fibonacci numbers
#      lis = [0,1]
#      for i in range(2,n):
#          lis.append(lis[i-2] + lis[i-1])
#      return(lis[0:n])
#
# print(sum(F(2000000)))

# But better

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

F(2000000)
# ---------------------------------------------------------------------------- #
#                                 13/02/2019/
# ---------------------------------------------------------------------------- #
