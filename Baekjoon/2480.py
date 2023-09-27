f = open('2480.txt')

n = list(map(int,f.readline().split()))
print(n)

a = n[0]
b = n[1]
c = n[2]

#print(a)
#print(b)
#print(c)

price = 0

if a == b == c :
    price += (10000 + a * 1000)
elif a == b:
    price += (1000 + a * 100)
elif b == c:
    price += (1000 + b * 100)
elif a == c :
    price += (1000 + a * 100)
else:      
    price += (max(a,b,c) * 100)

print(price)