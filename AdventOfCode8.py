def part1(list):
    accumulatorValue = 0
    position = 0
    visited = []
    stop = True
    while stop:
        if position in visited:
            stop = False
        visited.append(position)
        a = list[position]
        if a[0] == 'acc':
            if a[1][0] == '+':
                accumulatorValue = accumulatorValue + int(a[1][1:])
            if a[1][0] == '-':
                accumulatorValue = accumulatorValue - int(a[1][1:])
            position = position + 1
        if a[0] == 'jmp':
            if a[1][0] == '+':
                position = position + int(a[1][1:])
            if a[1][0] == '-':
                position = position - int(a[1][1:])
        if a[0] == 'nop':
            position = position + 1

    return accumulatorValue


def part2(list):
    pass
def hasLoop(list):
    pass

f = open('AOC8.txt', 'r')
data = f.read().splitlines()
f.close()

list = []

for item in data:
    list.append(item.split())

print(part1(list))
part2(list)

#print(allDone)