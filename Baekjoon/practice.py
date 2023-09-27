import sys

f = open('2750.txt')

T = int(f.readline())
# print(T)




l= []
for i in range(1, T+1):
    a = i
    l += (list(map(int, f.readline().rstrip().split())))
    if a == T:
        list = l
        print(l)
        for j in range(1, T+1):
            b = min(l)
            print(b)
            l - [min(l)]