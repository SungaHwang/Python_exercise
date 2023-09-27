f = open('input.txt')

N = int(f.readline())
numbers = list(map(int,f.readline().split()))

print(N)
print(numbers)

a = 0
for i in numbers:
    x = False
    if i == 1:
        continue
    elif i == 2:
        a += 1
    else:
        for j in range(2,i):
            if i % j == 0:
                x = True
                break
        if x == False:
            a += 1

print(a)