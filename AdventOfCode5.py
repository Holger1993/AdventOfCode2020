def row(str,range):
    mid = int(len(range)/2)
    #print(str, range)
    if len(str) == 1:
        if str == 'F':
            return range[0]
        elif str == 'B':
            return range[1]
    if str[0] == 'F':
        return row(str[1:],range[:mid])
    elif str[0] == 'B':
        return row(str[1:],range[mid:])

def column(str,range):
    mid = int(len(range)/2)
    #print(str, range)
    if len(str) == 1:
        if str == 'L':
            return range[0]
        elif str == 'R':
            return range[1]
    if str[0] == 'L':
        return column(str[1:],range[:mid])
    elif str[0] == 'R':
        return column(str[1:],range[mid:])

f = open('AOC5.txt', 'r')
lines = f.readlines()
f.close()

rowRange = list(range(0,128))
colRange = list(range(0,8))

highseatID = 0
allseatID = []

for boardID in lines:
    rowcol = [row(boardID[0:7],rowRange),column(boardID[7:10],colRange)]
    seatID = rowcol[0]*8 + rowcol[1]
    allseatID.append(seatID)
    if seatID > highseatID:
        highseatID = seatID
print(highseatID)
allseatID.sort()

c = 0
for i in range(min(allseatID),len(allseatID) + min(allseatID)):
    if i != allseatID[c]:
        print(i)
        break
    c += 1