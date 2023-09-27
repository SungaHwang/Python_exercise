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
                count += 1
                return x, y-1-i, count
    elif d == 'D':
        for i in range(0, A-y-1):
            if T[y+1+i][x] == '#':
                count += 1
                return x, y+i, count
            elif T[y+1+i][x] == 'O':
                count += 1
                return x, y+1+i, count
    elif d == 'R':
        for i in range(0, B-x-1):
            if T[y][x+1+i] == '#':
                count +=1
                return x+i, y, count
            elif T[y][x+1+i] == 'O':
                count += 1
                return x+1+i, y, count
    elif d == 'L':
        for i in range(0, x):
            if T[y][x-1-i] == '#':
                count += 1
                return x-i, y, count
            elif T[y][x-1-i] == 'O':
                count +=1
                return x-1-i, y, count


def observe(X_R, Y_R, count):
    D = ['U', 'D', 'R', 'L']
    x, y = X_R, Y_R

    for i in range(0, 4):
        x_next, y_next, count = end_point(x, y, D[i], count)
        # print(D[i], x, y, x_next, y_next)
        if not (x == x_next and y == y_next):
            # print(x_next, y_next)
            observe(x_next, y_next, count)

        else:
            count -= 1

    print(count)


for i in range(0, A):
    X_R, Y_R = 0, 0

    if 'R' in T[i]:
        Y_R = i
        X_R = T[i].index('R')

        observe(X_R, Y_R, 0)