f = open('2439.txt')
N = int(f.readline())

a = '*'
b = ' '
for i in range(1, N+1):
    print(b*(N-i)+a*i)