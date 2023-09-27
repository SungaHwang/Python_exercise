f = open('155552.txt')

T = int(f.readline().rstrip())

for i in range(2,T+2):
    L = (list(map(int,f.readline().rstrip().split())))
    add = L[0] + L[1]
    print(add)

