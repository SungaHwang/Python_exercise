import sys
f = sys.stdin

f = open('11021.txt')
T = int(f.readline().rstrip())

for i in range(2, T+2):
    C = (list(map(int, f.readline().rstrip().split())))
    add = C[0] + C[1]
    n = i-1
    print(f"Case #{n}: {add}")
