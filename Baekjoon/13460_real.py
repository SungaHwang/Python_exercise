f = open('13460.txt')

A, B = (map(int, f.readline().rstrip().split()))

T = []

for i in range(0, A):
    L = list((f.readline().rstrip()))
    T.append(L)
print(T)

def end_point(x, y, d, count):
    if d == 'U':
        for i in range(0, y):
            if T[y-1-i][x] == '#':
                count +=1
                return x, y-i, count
            elif T[y-1-i][x] == 'O':
                return x, y-1-i, count
    elif d == 'D':
        for i in range(0, A-y-1):
            if T[y+1+i][x] == '#':
                count += 1
                return x, y+i, count
            elif T[y+1+i][x] == 'O':
                return x, y+1+i
    elif d == 'R':
        for i in range(0, B-x-1):
            if T[y][x+1+i] == '#':
                count +=1
                return x+i, y, count
            elif T[y][x+1+i] == 'O':
                return x+1+i, y
    elif d == 'L':
        for i in range(0, x):
            if T[y][x-1-i] == '#':
                count += 1
                return x-i, y, count
            elif T[y][x-1-i] == 'O':
                return x-1-i, y

def observe(X_O, Y_O, X_R, Y_R, X_B, Y_B):
    l = []

    if T[Y_R][X_R] == 'O':
        count +=1
        return count
        
    D = ['U', 'D', 'R', 'L']
    for i in range(0, 4):
        count = 0
        x, y, count = end_point(X_R, Y_R, D[i], count)
        observe(X_O, Y_O, x, y, X_B, Y_B)
        l.append(count)
    print(l)

for i in range(0, A):
    X_O, Y_O, X_R, Y_R, X_B, Y_B = 0, 0, 0, 0, 0, 0

    if 'O' in T[i]:
        Y_O = i
        X_O = T[i].index('O')
    
    if 'B' in T[i]:
        Y_B = i
        X_B = T[i].index('B')

    if 'R' in T[i]:
        Y_R = i
        X_R = T[i].index('R')

        observe(X_O, Y_O, X_R, Y_R, X_B, Y_B)





