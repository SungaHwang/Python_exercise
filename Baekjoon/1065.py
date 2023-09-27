import math

def solve(a):
    l = []
    hansum_num = 0
    if a <= 99:
        hansum_num += 1
    elif a == 1000:
        pass
    else:
        for i in range(0, len(str(a))):
            l.append(math.floor(a % (10 ** (i+1)) / (10**(i))))
        # print(l)
        if l[1] - l[0] == l[2] - l[1]:
            hansum_num += 1
    return hansum_num

N = input()
total = 0
for j in range(1, N+1):
    total += (solve(j))

print(total)