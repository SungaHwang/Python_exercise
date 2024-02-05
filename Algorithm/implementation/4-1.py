f = open('Algorithm/implementation/4-1.txt')

n = int(f.readline())
x, y = 1, 1
plans = f.readline().split()

#print(n)
#print(plans)

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 밖 넘어가는 경우
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
        
    