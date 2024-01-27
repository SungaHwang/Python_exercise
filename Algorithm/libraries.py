# itertools
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

from itertools import combinations
result = list(combinations(data, 2)) # 2개를 뽑는 조합 구하기
print(result)

from itertools import product
result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 (중복 허용)
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# heapq
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# bisect - 이진탐색
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x)) # 정렬 순서는 유지하면서 가장 왼쪽으로 인덱스 값 지정
print(bisect_right(a, x)) # " 오른쪽

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

# collections
from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# math
import math
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(math.pi)
print(math.e)
