def part1(temp):
    holdingGold = ['shiny gold']
    goOn = True
    start = len(temp)
    for line in temp:
        a = line.split((' bags contain '))
        if 'shiny gold' in a[1]:
            #print(line)
            holdingGold.append(a[0])
            temp.remove(line)

    listlen = len(temp)
    newlistlen = 0
    while listlen != newlistlen:
        listlen = len(temp)
        for line in temp:
            a = line.split((' bags contain '))
            for hold in holdingGold:
                if hold in a[1]:
                    holdingGold.append(a[0])
                    temp.remove(line)
                    break
        newlistlen = len(temp)
    print(start - len(temp))

def part2(bagInfo, amount):
    pass

def addRelevant(bagInfo):
    global relevant
    global onlylist
    for line in relevant:
        a = line.split(' contain ')
        if a[0] == bagInfo:
            onlylist.append(line)
            if a[1] != 'no other':
                b = a[1].split(', ')
                for c in b:
                    addRelevant(c[2:])


f = open('AOC7.txt', 'r')
temp = f.read().splitlines()
f.close()
part1(temp)

relevant = []

onlylist = []

for line in temp:
    line = line.replace(' bags.', '')
    line = line.replace(' bag.', '')
    line = line.replace(' bags', '')
    relevant.append(line)

addRelevant('shiny gold')

print(len(onlylist))
c = 0
while onlylist:
    a = onlylist[0].split(' contain ')

a = onlylist[0].split(' contain ')
b = a[1].split(', ')
print(b)