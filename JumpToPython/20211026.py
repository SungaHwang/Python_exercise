#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:06:23 2021

@author: sungahwang
"""

# 딕셔너리

dic = {'name':'aaa', 'mobile':'01012345678', 'birth':'1010'} # key값: vlaue값
print(dic)

a = {'a':[1, 2, 3]} # value에 list값 가능
print(a)

dic['email'] = 'aaa@aaa.com' # email 추가
print(dic)

del dic['email'] # email 삭제
print(dic)

dic['name'] # name 의 value값 출력

a = {'a':1, 'a':2} # 중복되는 key값 -> error
print(a) # 뒤에 있는 값만 살아남음 (덮어쓰기)

a = {[1, 2, 3]: [4, 5, 6]} # key값으로는 list 불가

dic.keys()
list(dic.keys()) # list로 바꿔 출력
tuple(dic.keys()) # tuple로 바꿔 출력

dic.values()
list(dic.values())
tuple(dic.values())

dic.items()
list(dic.items())
list(dic.keys())

dic['name']
dic.get('name')
# 없는 값을 가져올때 차이를 보임
dic['email'] # error
dic.get('email') #아무것도 출력x

dic.get('email', 999) # 없는 값을 찾을 때 값 넣어줄 수 있음
dic.get('name', 999)

'name' in dic # 안에 name key가 있는지 없는지
'email' in dic

'aaa' in dic

'aaa' in dic.values() # 안에 aaa value가 있는지 없는지

s1 = set([1, 2, 3]) # 집합자료형
print(s1)

s2 = {1, 2, 3}
print(s2)

type(dic)
type(s1)
type(s2)

s3 = set("World") # 문자형
s3 # 집합 자료형은 순서가 없음

s4 = set("Apple")
print(s4) # 중복을 허용하지 않음

dic[0] # 인덱싱 넘어 error
dic['name'] # key값으로

s4[0]

l4 = list(s4)
l4[0]
print(l4)
t4 =tuple(s4)
t4[0]

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2 # 교집합
s2 & s1

s1.intersection(s2)# 교집합
s2.intersection(s1)

s1 | s2 # 합집합
s2 | s1
s1.union(s2)# 합집합
s2.union(s1)
    
s1 - s2 #차집합
s2 - s1
s1.difference(s2)
s2.difference(s1)
    
s1
s1.add(7) # 7추가
print(s1)
s1.add(8, 9) # 8,9 추가

s1.add(8)
s1.add(9)
print(s1)

s1.update([10, 11, 12])
print(s1)

s1.remove(7) # 7지우기
print(s1)

s4
s4.remove('p') # p지우기
print(s4)

l1 = [2, 5, 5, 8, 8, 3, 6, 3, 2]
l1_new = list(set(l1)) # 집합으로 만들고 다시 리스트로
print(l1_new) # 중복제거

# 불 자료형 (TRUE, FALSE)
a = True
b = False
type(a)
type(b)

# 조건문의 반환값으로 주로 사용
1 == 1
2 == 1

type(1 == 1)
type(1 == 2)
type(2 > 1)
type(2 < 3)

bool("") # False
bool("a")
bool() # False
bool(None) # False
bool(0) # 0도 False
bool(1)
bool(100)

bool([]) # False
bool([1, 2, 3])
bool(()) # False
bool((1, 2))
bool({}) # False

a = [1, 2, 3]
a_new = a # 복사본 만들기
print(a_new)
a_new[1] = 4
print(a_new)
print(a) # 이렇게 복사본을 만들면 연동이 되어있음

a_new = a[:] # 전체 출력
print(a_new) # 복사본
a_new[1] = 2
print(a_new)
print(a) # 연동 되지 않음


from copy import copy # 외장함수
 
a_new2 = copy(a) # 복사본
print(a_new2)
a_new2[1] = 9
print(a_new2)
print(a) # 연동 안됨


a, b = 'python', 'R'
print(a) # python
print(b) # R

[a, b] = ['banana', 'apple']
print(a) #banana
print(b) #apple

a = b = "python"
print(a)
print(b)

a = 3
b = 5
a, b = b, a # 값 맞바꾸기
print(a)
print(b)


# 제어문

score = 80
if score >= 90:
    print("A")
else:
    print("B") # 90이상이면 A, 아니면 B
    
if score >= 90:
    print("A+")
    print("A0")
else:
    print("B+")
    print("B0") # 두개 다 실행
    

if score >= 95:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 85:
    print("B+")
else:
    print("B") # 95이상 A+, 90이상 A, 85이상 B+ 아니면 B
  
"""
R과 동일
<
>
<=
>=
==
!=
"""

score = 97
if score >= 95 and score <= 100:
    print("A+") #그리고

if score > 95 or socre == 95:
    print("A+") #또는

grade_list = ["A", "A+", "A+", "B+"]

"A" in grade_list
"C" in grade_list

if "A" in grade_list:
    print("Good!") # 안에 있으면 출력
    
if "C" not in grade_list:
    print("Good!") # 안에 없으면 출력
    
score = 90
if score >= 95 and score <= 100:
    pass
else:
    print("T_T") # 95~100이면 pass 아니면 출력
    

if socre >= 95:
    grade = "A+"
else:
    grade = "AB" # 95이상이면 A+, 아니면 AB로 할당
print(grade)

score = 97
grade = "A+" if score >= 95 else "AB" #위와 동일
print(grade)


# while문
# 나무를 열번찍어야 넘어간다
treeHit = 0
while treeHit < 10:
    #treeHit = treeHit + 1
    treeHit += 1 # 1씩 증가
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어간다.")

treeHit = 0
while treeHit >= 0:
    #treeHit = treeHit + 1
    treeHit += 1 # 1씩 증가
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어간다.") # 무한대로 실행(빨간색 네모표시로 멈추기)
        
treeHit = 0
while treeHit >= 0:
    #treeHit = treeHit + 1
    treeHit += 1 # 1씩 증가
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어간다.")
        break # if문이 실행 될 때 멈춤
        
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        print(a) #짝수 print
        
a = 0
while a < 10:
    a += 1
    if a % 2 == 1:
        print(a) #홀수 print
               
a = 0
while a < 10:
    a += 1
    if a % 2 == 1: continue
    print(a) #홀수 건너뛰기

