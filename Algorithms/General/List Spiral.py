n = int(input())
if n < 2: print(n)
else:
    matrix = [[0] * n for i in range(n)]

    row = 0; col = n-1; new = [] # indexes |
                                                                     #    Matrix(i,j)
    while row < n:
        new.extend([(row, _)     for _ in range(row, col-row)])      # i(min) |  j+     - right
        new.extend([(_, col-row) for _ in range(row, col-row)])      # i+     |  j(max) - down
        new.extend([(col-row, _) for _ in range(col-row, row, -1)])  # i(max) |  j-     - left
        new.extend([(_, row)     for _ in range(col-row, row, -1)])  # i-     |  j(min) - up
        row += 1

    if n % 2 == 1: new.append((n-int(n/2)-1, n-int(n/2)-1)) # Central element

    for i in range(1, n*n+1):
        matrix[new[i-1][0]][new[i-1][1]] = i

    for line in matrix:
        print(*line)
