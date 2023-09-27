# import sys
# f = sys.stdin

f = open('10952.txt')

while True:
    A, B = map(int, f.readline().split())
    if A == B == 0:
        break
    print(A+B)
