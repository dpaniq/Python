import time

# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    a = time.time()
    prime = [True]*n

    for i in range(2, len(prime)):
        if prime[i]:
            for j in range(i**2, n, i):
                if j <= n:
                    prime[j] = False

    x = [i for i in range(len(prime)) if prime[i] == True]

    return time.time() - a

print(sieve_of_eratosthenes(100000000))

# Atkins
# [not yet]
