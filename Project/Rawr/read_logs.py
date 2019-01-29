with open('logs.txt') as txt:
    f = txt.readlines()

count = 0
for i in f:
    if i.strip() == '':
        continue
    else:
        print(i.strip())
        count += 1

print(count / 4)
