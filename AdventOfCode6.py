def totAllYes(answears):
    if len(answears) == 1:
        return len(answears[0])
    else:
        ref = answears[0]
        answears.pop(0)
        allyes = len(answears)
        count = 0
        for char in ref:
            oneyes = 0
            for ans in answears:
                if char in ans:
                    oneyes = oneyes + 1
            if oneyes == allyes:
                count = count + 1
        return count

f = open('AOC6.txt', 'r')
temp = f.read().splitlines()
f.close()

a = []
c = 0
c2 = 0
for line in temp:
    if line == '':
        c = c + len("".join(set(''.join(a))))
        c2 = c2 + totAllYes(a)
        a = []
    else:
        a.append(line)
c = c + len("".join(set(''.join(a))))
c2 = c2 + totAllYes(a)
print(c)
print(c2)