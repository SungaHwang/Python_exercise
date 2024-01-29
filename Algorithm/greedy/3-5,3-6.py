# 1이 될 때까지 -> N과 K가 주어질 때 1이 될 떄 까지 (i) N에서 1을 뺀다, (ii) N을 K로 나눈다 
# 과정을 몇 번 수행해야 하는지 최소 횟수 출력

f = open('Algorithm/greedy/3-5.txt')
n, k = map(int, f.readline().split())

result = 0
while n > k :
    while n % k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

#
n, k = map(int, f.readline().split())

result = 0
while True:
    target = (n // k) * k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n // k
result += (n-1)

print(result)

"""
두 가지 방법으로 최소 횟수를 만드려면 나누는 과정을 최대한 많이 활용해야 함.
따라서 나눌 수 있게끔 K의 배수 만큼이 되게끔 조정을 먼저 하고 K로 나누는 방법을 반복하고
n이 k보다 작아졌을 때는 1이 될 때까지 1씩 뺀다.
"""