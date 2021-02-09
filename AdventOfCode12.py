def part1(data):
    dir = 'E'
    rot = 0
    NSPos = 0
    WEPos = 0
    for i in data:
        if i[0] == 'N':
            NSPos += int(i[1:])
        if i[0] == 'S':
            NSPos -= int(i[1:])
        if i[0] == 'E':
            WEPos += int(i[1:])
        if i[0] == 'W':
            WEPos -= int(i[1:])
        if i[0] == 'L':

        if i[0] == 'R':

        if i[0] == 'F':


    return abs(NSPos) + abs(WEPos)
def part2():
    pass

f = open('AOC12.txt', 'r')
data = f.read().splitlines()
f.close()
a = ['F10','N3','F7','R90','F11']
print(part1(a))