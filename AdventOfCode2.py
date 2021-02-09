f = open('AOC2.txt', 'r')
lines = f.readlines()
f.close()
globalCount = 0

# Part 1
for i in lines:
    a = i.split()
    lims = a[0].split('-')
    char = a[1].split(':')
    counter = a[2].count(char[0])
    if counter >= int(lims[0]):
        if counter <= int(lims[1]):
            globalCount = globalCount + 1

print(globalCount)

# Part 2
globalCount2 = 0
for i in lines:
    a = i.split()
    str = a[2]
    pos = a[0].split('-')
    pos1 = int(pos[0])
    pos2 = int(pos[1])
    char = a[1].split(':')
    if str[pos1-1] == char[0]:
        if str[pos2-1] != char[0]:
            globalCount2 = globalCount2 + 1
    if str[pos2-1] == char[0]:
        if str[pos1-1] != char[0]:
            globalCount2 = globalCount2 + 1

print(globalCount2)

