# 큰 수의 법칙
# n개의 숫자를 가지고 m번 곱하는 식을 만드는데 한 데이터는 k번 씩만 가능 -> 최대 만들기

f = open('Algorithm/greedy/3-2.txt')
n, m, k = map(int, f.readline().split())
data = list(map(int, f.readline().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)

"""
숫자를 먼저 작은 -> 큰 순서대로 정렬을 하고, 가장 큰 숫자랑 가장 작은 숫자를 뽑는다.
가장 큰 곱을 만들라면 가장 큰 숫자를 당연히 젤 많이 곱해야 하는데 개수 제한이 있으니까
중간에 k의 제한이 끝나면 두 번쨰로 큰 숫자를 더하도록 한다. 그래서 패턴은 k+1 단위로 바뀐다.
전체 m 번을 곱해야 하니까 k+1 의 단위 패턴을 나누어 줘서 총 몇 번 패턴이 진행되는지를 확인.
몫 만큼은 총 패턴이고 나머지 만큼은 추가로 진행해야할 덧셈
첫 번째 큰 숫자를 더하는게 젤 중요하고 첫 번쨰 숫자를 더하는 것이 아닌 모든 숫자는 두 번째 숫자가 될 것
그럼 result를 0으로 초기값을 둬서 count 개수 만큼 첫 번째 큰 숫자를 더하고
m-count만큼 두 번째 큰 숫자를 더해서 최종 결과를 구한다.
"""