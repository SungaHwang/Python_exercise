#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:53:46 2021

@author: sungahwang
"""

# for 문
test_list = ['a', 'b', 'c'] #list생성

for i in test_list:
    print(i) #list에 있는 요소들이 순서대로 i에 들어옴

a = [(1, 2), (3, 4), (5, 6)] # tuple로 묶여있는 list생성
 
for i in a:
    print(i)
    
for (first, last) in a:
    print(first + last) #합 구하기

scores = [90, 80, 70, 65, 55]
num = 0 # 초기값

for score in scores:
    num += 1
    if score >= 70:
        print("%d번 학생 합격" % num)
    else:
        print("%d번 학생 불합격" % num) #각 번호의 학생이 70점 이상이면 합격, 아니면 불합격
        
        
scores = [90, 80, 70, 65, 55]
num = 0 # 초기값

for score in scores:
    num += 1
    if score < 70: continue
    print("%d번 학생 합격" % num) #70이상만 print문 실행
    

range(10) # 끝만 지정하면 0부터 시작
range(1, 10) # 시작, 끝 숫자 지정

for j in range(10):
    print(j) # 0부터 9

for k in range(1, 10):
    print(k) # 1부터 9
    
range(len(scores))
# range(5) 위와 같음

for num in range(len(scores)):
    if scores[num] < 70: continue
    print("%d번 학생 합격" % (num + 1)) #70이상만 print문 실행(인덱싱 활용)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ") # 한칸 띄우기
    print('') # 줄바꿈

a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num * 3) # result에 각각 3곱한 값 추가
    
result

a = [1, 2, 3, 4]
result = [num * 3 for num in a] #곧바로 list 안에
result

result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3) # 짝수만 3곱해서 추가
result

result = [num * 3 for num in a if num % 2 == 0] #곧바로 list 안에(짝수만)
result

# 구구단
result = []
for i in range(2, 10):
    for j in range(1, 10):
        result.append(i * j)
print(result)


result = [i * j for i in range(2, 10)
          for j in range(1, 10)] # list 내포

print(result)