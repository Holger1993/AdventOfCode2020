def part1(list):
    num = 25
    goOn = True
    while goOn:
        num = num + 1
        shortList = list[num-25:num]
        goOn = findPair(shortList, int(list[num]))
    return list[num]

def findPair(list, num):
    for i in list:
        for j in list:
            if int(i) + int(j) == num:
                return True
    return False

def part2(list, find):
    low = 0
    high = 2
    goOn = True
    while goOn:
        count = 0
        for i in range(low, high):
            count = count + int(list[i])
        if count < find:
            high = high + 1
        if count > find:
            low = low + 1
            high = low + 2
        if count == find:
            goOn = False
            count = findLowHighSum(list[low:high])
    return count

def findLowHighSum(lista):
    lista = list(map(int, lista))
    return min(lista) + max(lista)


f = open('AOC9.txt', 'r')
data = f.read().splitlines()
f.close()

print(part1(data))
print(part2(data, int(part1(data))))