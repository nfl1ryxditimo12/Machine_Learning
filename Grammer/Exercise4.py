import os

print('\n==================================================\n')#

# 문제 1
# 두개의 정숫값을 받아 두 값의 평균을 구하는 함수를 작성하세요.

def myaverage(a, b):
    avg = (a + b)/2

    return avg

print(myaverage(2, 4))

print('\n==================================================\n')

# 문제 2
# 함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정숫값에 대한 최댓값과 최솟값을 반환하는 함수를 작성하세요.

def get_max_min(data_list):
    max_list = max(data_list)
    min_list = min(data_list)

    return (max_list, min_list)

list = [1, 4, 5, 6, 3, 4, 7, 10, 2]

print(get_max_min(list))

print('\n==================================================\n')

# 문제 3
# 절대 경로를 입력받은 후 해당 경로에 있는 *.py파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.

# def get_py_list(path):
#     org_list = os.listdir(path)
#     ret_list = []
#     for x in org_list:
#         if x.endswith('py'):
#             ret_list.append(x)
#
#     return ret_list
#
# print(get_py_list('User/'))



print('\n==================================================\n')

# 문제 4
# 체질량 지수(BMI)는 인간의 비만도를 나타내는 지수로서 체중과 키의 관계로 아래의 수식을 통해 계산합니다. 여기서 중요한 점은 체중의 단위는 킬로그램이고 신장의 단위는 미터라는 점입니다.

def BMI(kg, m):
    bmi = kg / (m * m)

    if bmi >= 30.0:
        print('고도 비만')
    elif bmi >= 25.0:
        print('비만')
    elif bmi >= 18.5:
        print('표준')
    else:
        print('마른 체형')

print(BMI(88, 1.78))

print('\n==================================================\n')

# 문제 5
# 사용자로부터 키와 몸무게를 입력받은 후 BMI 값에 따른 체형 정보를 화면에 출력하는 프로그램을 작성해 보세요.
# 파이썬에서 사용자 입력을 받을 때는 input 함수를 사용하며, 작성된 프로그램은 계속해서 사용자로부터 키와 몸무게를 입력받은 후 BMI 및 체형 정보를 출력해야 합니다.


kg = int(input())
m = float(input())

print(BMI(kg, m))

print('\n==================================================\n')

# 문제 6
# 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성하세요.

def get_triangle_area(width, height):
    area = width * height / 2

    return area

print(get_triangle_area(10, 10))

print('\n==================================================\n')

# 문제 7
# 함수의 인자로 시작과 끝을 나타내는 숫자를 받아 시작부터 끝까지의 모든 정수값의 합을 반환하는 함수를 작성하세요.

def add_start_to_end(start, end):
    sum = 0

    for i in range(start, end + 1):
        sum += i

    return sum

print(add_start_to_end(10, 20))

print('\n==================================================\n')

# 문제 8
# 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스트를 반환하는 함수를 작성하세요.
# 예를 들어, 함수에 ['Seoul', 'Daegu', 'Kwangju', 'Jeju'] 가 입력될 때 함수의 반환값은 ['Seo', 'Dae', 'Kwa', 'Jej'] 입니다.

def city(list):
    result = []

    for i in range(len(list)):
        result.append(list[i][:3])

    return result

list = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']

print(city(list))

print('\n==================================================\n')