import copy

def part1(data):
    equal = True
    newData = copy.deepcopy(data)
    while equal:
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[0]) - 1):
                if data[i][j] == '.':
                    newData[i][j] = '.'
                if data[i][j] == 'L':
                    newData[i][j] = freeSpace(data,i, j)
                if data[i][j] == '#':
                    newData[i][j] = occupied(data,i, j)

        if newData == data:
            equal = False
        data = copy.deepcopy(newData)

    count2 = 0
    for i in newData:
        for j in i:
            if j == '#':
                count2 += 1
    return count2

def freeSpace(data,i,j):
    numN = countNeighbour(data,i,j)
    if numN == 0:
        return '#'
    return 'L'
def occupied(data,i,j):
    numN = countNeighbour(data,i,j)-1
    if numN > 3:
        return 'L'
    return '#'
def countNeighbour(data,i,j):
    count = 0
    for k in range(i-1,i+2):
        for l in range(j-1, j+2):
            if data[k][l] == '#':
                count += 1
    return count

def part2(data):
    equal = True
    newData = copy.deepcopy(data)
    while equal:
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[0]) - 1):
                if data[i][j] == '.':
                    newData[i][j] = '.'
                if data[i][j] == 'L':
                    newData[i][j] = freeSpace2(data, i, j)
                if data[i][j] == '#':
                    newData[i][j] = occupied2(data, i, j)

        if newData == data:
            equal = False
        data = copy.deepcopy(newData)

    count2 = 0
    for i in newData:
        for j in i:
            if j == '#':
                count2 += 1
    return count2


def freeSpace2(data, i, j):
    numN = countNeighbour2(data, i, j)
    if numN == 0:
        return '#'
    return 'L'


def occupied2(data, i, j):
    numN = countNeighbour2(data, i, j)
    if numN > 4:
        return 'L'
    return '#'


def countNeighbour2(data, i, j):
    count = 0
    step = 1
    goOn = True
    while goOn:
        if data[i-step][j-step] == '.':
            step += 1
        else:
            if data[i - step][j - step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i - step][j] == '.':
            step += 1
        else:
            if data[i - step][j] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i - step][j + step] == '.':
            step += 1
        else:
            if data[i - step][j + step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i][j - step] == '.':
            step += 1
        else:
            if data[i][j - step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i][j + step] == '.':
            step += 1
        else:
            if data[i][j + step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i + step][j - step] == '.':
            step += 1
        else:
            if data[i + step][j - step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i + step][j] == '.':
            step += 1
        else:
            if data[i + step][j] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    step = 1
    goOn = True
    while goOn:
        if data[i + step][j + step] == '.':
            step += 1
        else:
            if data[i + step][j + step] == '#':
                count += 1
                goOn = False
            else:
                goOn = False
    return count


f = open('AOC11.txt', 'r')
data = f.read().splitlines()
f.close()

#data = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']

for i in range(0,len(data)):
    data[i] = '.' + data[i] + '.'
    data[i] = list(data[i])
dot = '..'
for i in range(0,len(data)+1):
    dot = dot + '.'
data.append(list(dot))
data.insert(0,list(dot))
print(part1(data))

f = open('AOC11.txt', 'r')
data = f.read().splitlines()
f.close()

#data = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']

for i in range(0,len(data)):
    data[i] = 'L' + data[i] + 'L'
    data[i] = list(data[i])

dot = 'LLL'
for i in range(0,len(data)):
    dot = dot + 'L'
data.append(list(dot))
data.insert(0,list(dot))

print(part2(data))