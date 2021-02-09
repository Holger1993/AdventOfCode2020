f = open('AOC1.txt', 'r')
lines = f.readlines()
f.close()
# Part 1
for i in lines:
    for j in lines:
        if int(i)+int(j) == 2020:
            print(int(i)*int(j))

# Part 2
for i in lines:
    for j in lines:
        for k in lines:
            if int(i)+int(j)+int(k) == 2020:
                print(int(i)*int(j)*int(k))
