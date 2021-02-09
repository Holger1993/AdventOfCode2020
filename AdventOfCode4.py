def includingPart1(str):
    include = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    #print(str.split())
    c = 0
    for data in include:
        if data in str:
            c = c + 1
    if c == 7:
        return 1
    else:
        return 0

def includingPart2(str):
    divide = str.split()
    c = 0
    for info in divide:
        whatInfo = info.split(':')
        if whatInfo[0] == 'byr':
            c = c + BirthYear(int(whatInfo[1]))
        if whatInfo[0] == 'iyr':
            c = c + IssueYear(int(whatInfo[1]))
        if whatInfo[0] == 'eyr':
            c = c + ExpirationYear(int(whatInfo[1]))
        if whatInfo[0] == 'hgt':
            c = c + Height(whatInfo[1])
        if whatInfo[0] == 'hcl':
            c = c + HairColor(whatInfo[1])
        if whatInfo[0] == 'ecl':
            c = c + EyeColor(whatInfo[1])
        if whatInfo[0] == 'pid':
            c = c + PassportID(whatInfo[1])
    if c == 7:
        return 1
    else:
        return 0

def BirthYear(byr):
    # byr
    # four digits; at least 1920 and at most 2002.
    if byr >= 1920 and byr <= 2002:
        return 1
    else:
        return 0

def IssueYear(iyr):
    # iyr
    # four digits; at least 2010 and at most 2020.
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        return 1
    else:
        return 0

def ExpirationYear(eyr):
    # eyr
    # four digits; at least 2020 and at most 2030.
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return 1
    else:
        return 0
def Height(hgt):
    # a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    len = hgt[:-2]
    if hgt[-2:] == 'in' and int(len) >= 59 and int(len) <= 76:
        return 1
    elif hgt[-2:] == 'cm' and int(len) >= 150 and int(len) <= 193:
        return 1
    else:
        return 0

def HairColor(hcl):
    # a # followed by exactly six characters 0-9 or a-f.
    if hcl[0] == '#' and len(hcl) == 7:
        return 1
    else:
        return 0

def EyeColor(ecl):
    # exactly one of: amb blu brn gry grn hzl oth.
    ecllist = ['amb','blu','brn','gry','grn','hzl','oth']
    if ecl in ecllist:
        return 1
    else:
        return 0

def PassportID(pid):
    # a nine-digit number, including leading zeroes.
    if len(pid) == 9:
        return 1
    else:
        return 0

def CountryID(cid):
    # ignored, missing or not.
    pass



f = open('AOC4.txt', 'r')
lines = f.readlines()
f.close()
print(len(lines))
allpassports = []
a = []
counter1 = 0
counter2 = 0
for line in lines:
    a.append(line)
    if line == '\n':
        allpassports.append(''.join(a))
        counter1 = counter1 + includingPart1(''.join(a))
        counter2 = counter2 + includingPart2(''.join(a))
        a = []

counter1 = counter1 + includingPart1(''.join(a))
counter2 = counter2 + includingPart2(''.join(a))

print(counter1)
print(counter2)