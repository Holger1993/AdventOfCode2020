f = open('AOC3.txt', 'r')
lines = f.readlines()
f.close()

# Part 1
xpos = 0
ypos = 0
counter = 0
while ypos < 323:
    #print(xpos,ypos)
    if lines[ypos][xpos] == '#':
        counter = counter + 1
    xpos = (xpos+3)%31
    ypos = ypos + 1

print(counter)

# Part 2
xjump = [1, 3, 5, 7, 1]
yjump = [1, 1, 1, 1, 2]
counts = [0, 0, 0, 0, 0]
for i in range(5):
    xpos = 0
    ypos = 0
    while ypos < 323:
        #print(xpos,ypos)
        if lines[ypos][xpos] == '#':
            counts[i] = counts[i] + 1
        xpos = (xpos+xjump[i])%31
        ypos = ypos + yjump[i]

print(counts[0]*counts[1]*counts[2]*counts[3]*counts[4])
