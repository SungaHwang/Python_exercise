# a = d(n) 생성자 X -> 셀프넘버 87 a<= 10000
# n: 생성자 75

self_num = []

def d(n):
    num = n
    for i in range(0, len(str(n))):
        num += int(n/10 ** i) % 10
    return num

for j in range(1, 10001):
    self_num.append(d(j))
    if j not in self_num:
        print(j)