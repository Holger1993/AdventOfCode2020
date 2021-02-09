def part1(input):
    input.append(0)
    input.sort()
    step1 = 0
    step3 = 0
    for i in range(0,len(input)-1):
        if input[i+1] - input[i] == 1:
            step1 += 1
        if input[i+1] - input[i] == 3:
            step3 += 1
    return step1 * (step3+1)

def part2(input):
    input.append(0)
    input.sort()
    index = 0
    print(pointTo(index, input))

def pointTo(index, input):
    if input[index] == 19:
        return 1
    count = 0
    for i in range(1,4):
        if input[index+i] - input[index]<=3:
            count = count + pointTo(index+1,input[index+1:])
    return count

f = open('AOC10.txt', 'r')
data = f.read().splitlines()
f.close()

a = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

b = [16,10,15,5,1,11,7,19,6,12,4]
b.sort()
print(b)
print(part1(list(map(int, data))))
print(part2(b))
# print(part2(list(map(int, data))))