d = {}
# d[country] = [win, lose, draw]

def addtodict(country1, country2, flag=0):
    if country1 not in d: d[country1] = [0] * 3
    if country2 not in d: d[country2] = [0] * 3

    if not flag:
        d[country1][0] += 1   # Plus win
        d[country2][1] += 1   # Plus lose
    else:
        d[country1][2] += 1   # Plus draw
        d[country2][2] += 1   # Plus draw

for i in range(int(input())):
    c1, score1, c2, score2 = input().split(';')

    if int(score1) > int(score2):   addtodict(c1, c2)    # win
    elif int(score1) < int(score2): addtodict(c2, c1)    # lose
    else:                           addtodict(c1, c2, 1) # draw (flag = 1)

for i in d:
    # [all, win, draw, lose, points]
    all = d[i][0] + d[i][1] + d[i][2]
    points = d[i][0]*3 + d[i][2]
    print(f'{i}:{all} {d[i][0]} {d[i][2]} {d[i][1]} {points}')

# Team: Total_games Wins Draws Total_ points

# 35
# France; 1; Romania; 1
# Albania; 0; Switzerland; 1
# Wales; 2; Slovakia; 1
# England; 1; Russia; 1
# Turkey; 0; Croatia; 1
# Poland; 1; Northern Ireland; 0
# Germany; 2; Ukraine; 0
# Spain; 1; Czech Republic; 0
# Belgium; 0; Italy; 2
# Austria; 0; Hungary; 2
# Portugal; 1; Iceland; 1
#Russia; 1; Slovakia; 2
# Romania; 1; Switzerland; 1
# France; 2; Albania; 0
# England; 2; Wales; 1
# Ukraine; 0; Northern Ireland; 2
# Germany; 0; Poland; 0
# Italy; 1; Sweden; 0
# Czech Republic; 2; Croatia; 2
# Spain; 3; Turkey; 0
# Belgium; 3; Ireland; 0
# Iceland; 1; Hungary; 1
# Portugal; 0; Austria; 0
# Switzerland; 0; France; 0
# Romania; 0; Albania; 1
# Slovakia; 0; England; 0
# Russia; 0; Wales; 3
# Northern Ireland; 0; Germany; 1
# Ukraine; 0; Poland; 1
# Croatia; 0; Spain; 1
# Czech Republic; 0; Turkey; 2
# Hungary; 0; Portugal; 3
# Iceland; 2; Austria; 1
# Sweden; 1; Belgium; 1
# Italy; 2; Ireland; 1
