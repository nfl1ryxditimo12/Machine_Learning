print('==================================================\n')

# 문자열

mystring = 'hello world'
print(mystring)

print('\n==================================================\n')

# 문자열 슬라이싱
# 말그대로 문자열을 잘라서 표현할 수 있는 방식

print(mystring[0:5])    # 문자열을 4번째 까지만 출력하는 표현
print(mystring[6:11])   # 문자열을 11번쨰 까지 출력하는 표현
print(mystring[:5])     # 안쓰면 처음부터 / 마지막까지

print('\n==================================================\n')

# 문자열 자르기

print(mystring.split(' '))      # split(' ') ' 과 ' 사이의 기호를 기준으로 문자열을 나눔
print(mystring.split(' ')[0])   # 나눈 문자열의 첫번째 리스트를 출력함

print('\n==================================================\n')

# 문자열 합치기

daum = 'Daum'
kakao = 'KAKAO'

print(daum+' '+kakao)