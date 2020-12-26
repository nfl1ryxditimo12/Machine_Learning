import module
import time
import random
import os

print('\n==================================================\n')

# 함수

def print_ntimes(n):
    for i in range(n):
        print('대신증권')

print(print_ntimes(1))

print('\n==================================================\n')

# 반환값이 있는 함수

def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment

    return upper_price

print(cal_upper(10000))

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement

    return lower_price

print(cal_lower(10000))

def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset

    return (upper, lower)

print(cal_upper_lower(20000))
(upper, lower) = cal_upper_lower(10000)
print(upper)
print(lower)

print('\n==================================================\n')

# 모듈

print(module.author)
print(module.module_lower(10000))
print(module.module_upper(10000))

print('\n==================================================\n')

# 파이썬에서 시간 다루기

print(time.ctime())

for i in range(1):
    print(i)
    time.sleep(1)

print(time)
print(random)
print(dir(time))
print(os.getcwd())
print(os.listdir())

for i in os.listdir():
    if i.endswith('py'):
        print(i, end=' ')
print('')

print('\n==================================================\n')

# 파이썬 내장 함수

print(abs(-3))      # abs 내장함수는 정수형 또는 실수형 값을 받은 후 절대 값으로 반환하는 함수이다.
print(abs(-3.0))

print(chr(97))      # chr 내장함수는 유니코드 값을 입력받은 후 그 값에 해당하는 문자열을 반환하는 함수이다.
print(chr(65))

for i, stock in enumerate(['Naver', 'KAKAO', 'SK']):    # enumerate 내장함수는 입력으로 시퀀스 자료형(리스트, 튜플, 문자열) 등을 입력받은 후 객체를 반환하는 함수이다.
    print(i, stock)

a = 1
b = 1
print(id(a))        # id 내장함수는 객체를 입력받아 해당 객체의 고윳값을 반환하는 함수이다.
print(id(b))

mystock = ['Naver', 'Samsung', 'SK', 'Daum', 'Apple', 'IBM', 'AT&T']
print(len(mystock))        # len 내장함수는 리스트, 튜플, 문자열, 딕셔너리 등을 입력받아 해당 객체의 원소 개수를 반환합니다.

print(list('Hello'))       # list 내장함수는 문자열이나 튜플을 입력받은 후 리스트 객체로 만들고 해당 리스트를 반환합니다.
print(list((1, 2, 3)))

print(max(1, 2, 3))        # max 내장함수는 입력값 중 최댓값을 반환합니다.
print(min(1, 2, 3))        # min 내장함수는 입력값 중 최솟값을 반환합니다.

print(sorted((4, 3, 2, 9, 0)))      # sorted 내장함수는 입력값을 정렬한 후 정렬된 결괏값을 리스트로 반환합니다.
print(sorted([5, 4, 3, 2, 1]))
print(sorted(['c', 'b', 'a']))

print(type(int('3')))            # int 내장함수는 입력값을 정수형으로 반환합니다.
print(type(str(3)))              # str 내장함수는 입력값을 문자열로 반환합니다.