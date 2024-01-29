# 숫자 카드 게임
f = open('Algorithm/greedy/3-3.txt')

n, m = map(int, f.readline().split())

result = 0
for i in range(n):
    data = list(map(int, f.readline().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


"""
n개의 행을 for문으로 받아서 각 행 마다 가장 작은 숫자를 선택하고, 다음 줄의 행에서 그 각 행에서의 작은 숫자가
그 전의 행보다 더 크다면, 그 숫자를 result 로 받아서 출력한다.
"""

# 2중 반복문
result = 0
n, m =  map(int, f.readline().split())
for i in range(n):
    data = list(map(int, f.readline().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result) 

"""
n으로 행의 개수를 for 문으로 받은 다음에, 각 숫자는 1~10000 까지만 존재할 수 있으니까
가장 최소 값을 먼저 10001로 초기값을 설정한 다음에, 각 행 안에서 for문으로 하나씩 확인해가면서 더 작은 수를 선택할 수 있게 한다.
그 다음에 행의 개수를 for 문으로 받은 쪽으로 빠져나와서 행 간의 값을 구할 수 있도록 한다.
"""