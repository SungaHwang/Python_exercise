f = open('1110.txt')
N = int(f.readline())
print(N)

M = N

n = 0
while True:
    a = M % 10
    b = ((M // 10) + a) % 10
    num = (a * 10) + b
    n += 1
    if num == N:
        break
    M = num
print(n)