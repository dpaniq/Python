# Insertion sort
# Example: "18 17 20 16 26 8 30 2 3 13"

A = list(map(int,input().split()))

for j in range(1, len(A)):
    key = A[j]
    i = j-1
    while (i >= 0 and A[i] > key):
        A[i + 1] = A[i]
        i = i - 1
    A[i+1] = key

print(*A)
