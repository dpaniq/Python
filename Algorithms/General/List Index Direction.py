m = []
while 1:
    line = input()
    if line == 'end': break
    else: m.append(list(map(int, line.split())))

row, col = len(m), len(m[0])

for i in range(row):
    for j in range(col):
        x = sum([m[i-1][j], m[i-row+1][j], m[i][j-1], m[i][j-col+1]])
        print(x, end = ' ')
    print()
