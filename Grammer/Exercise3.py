print('\n==================================================\n')#

# 문제 1
# 별(*)을 출력하는 프로그램을 작성해 보세요.

for i in range(5):
    print('*', end='')

print('\n==================================================\n')

# 문제 2
# 중첩 루프를 통한 별을 작성해 보세요.

for i in range(5):
    for j in range(5):
        print("*", end='')
    print("")

print('\n==================================================\n')

# 문제 3
# 갈수록 많아지는 별을 출력하는 프로그램을 작성해 보세요.

for i in range(5):
    for j in range(i + 1):
        print("*", end='')
    print("")

print('\n==================================================\n')

# 문제 4
# 갈수록 적어지는 별을 출력하는 프로그램을 작성해 보세요.

for i in range(5):
    for j in range(5 - i):
        print("*", end='')
    print("")

print('\n==================================================\n')

# 문제 5
# 반대쪽으로 많아지는 별을 출력하는 프로그램을 만들어 보세요.

for i in range(5):
    for j in range(5):
        if j >= 4 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print('\n==================================================\n')

# 문제 6
# 반대쪽으로 점차 줄어드는 별을 출력하는 프로그램을 만들어 보세요.

for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print('\n==================================================\n')

# 문제 7
# 피라미드 모양의 별을 출력하는 프로그램을 만들어 보세요.

for i in range(5):
    for j in range(5):
        if j >= 4 - i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')

print('\n==================================================\n')

# 문제 8
# 역방향 피라미드 모양의 별을 출력하는 프로그램을 만들어 보세요.

for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(4 - i):
        if j <= 4 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print('\n==================================================\n')

# 문제 9
# 중첩 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요.
# 단, arrears 리스트는 신문 구독료가 미납된 세대에 대한 정보를 포함하고 있는데, 해당 세대에는 신문을 배달하지 않아야 합니다.

apart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
    [401, 402, 403, 404],
]
arrears = [101, 203, 301, 404]
floor = 1

for i in apart:
    print("%d층 배달이요 : " % floor, end='')
    for j in i:
        if j == 101 or j == 203 or j == 301 or j == 404:
            continue
        print("%s호" % j, end=' ')
    floor += 1
    print('')
    
print('\n==================================================\n')