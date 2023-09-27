import sys

f = open('10872.txt')

T = int(f.readline())
#print(T)

b = 1

if T == 0:
    print(1)
else:
    for i in range(1, T+1):
        a = i
        b *= i
        if a ==T:
            print(b)



