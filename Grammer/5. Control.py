print('\n==================================================\n')

# Boolean

a = True
b = False
print(type(a))
print(type(b))
print(3 == 3)       # 3과 3이 같으면 True 다르면 False
print(3 != 3)
print(3 > 3)

mystock = 'Naver'
print(mystock == 'Naver')   # mystock 과 'Naver' 이 같으면 True 다르면 False

print('\n==================================================\n')

# 논리 연산자

cur_price = 9980

print(5000 <= cur_price < 10000)

day1 = 10000
day2 = 13000
print(((day2 - day1) == (day1 * 0.3)) or ((day2 - day1) > (day1 * 0.292)))

print('\n==================================================\n')

# if 문

wikibooks_cur_price = 11000
if wikibooks_cur_price >= 10000:
    print("buy 10 wikibooks")

wikibooks_cur_price = 8000
if wikibooks_cur_price < 9000:
    print("sell 10 wikibooks")

# if ~ else 문

if wikibooks_cur_price > 9000:
    print("buy 10 wikibooks")

else:
    print("holding")

# if ~ elif ~ else 문

wikibooks_cur_price = 3000

if wikibooks_cur_price > 10000:
    print('buy 10 wikibooks')

elif wikibooks_cur_price < 5000:
    print('sell 10 wikibooks')

else:
    print('holding')

print('\n==================================================\n')

# for 문

for i in range(10):
    print(i, end=' ')

print("\n")

# for 와 리스트

interest_stocksL = ['Naver', 'Samsung', 'SK Hynix']

for company in interest_stocksL:
    print("%s: Buy 10" % company)

# for 와 튜플

interest_stocksT = ('Naver', 'Samsung', 'SK Hynix')

for company in interest_stocksT:
    print("%s: buy 10 tuple" % company)

# for 와 딕셔너리

interest_stocksD = {
    'Naver': 10,
    'Samsung': 5,
    'SK Hynix': 30,
}

for company, stock_num in interest_stocksD.items():
    print("%s: Buy %d dic" % (company, stock_num))

print('\n==================================================\n')

# while 문

i = 0
while i < 10:
    print(i, end=' ')
    i +=1
print('\n')

day = 1
stock = 10000
while day < 6:
    stock += (stock * 0.3)
    day += 1

print(stock)

# while 과 if 의 동시 사용

i = 1
while i <= 10:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
print('\n')

# 무한루프

num = 0
while 1:
    print(num, end=' ')
    if num == 10:
        break
    num += 1
print('\n')

num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num, end=' ')

print('\n==================================================\n')

# 중첩 루프

apart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
    [401, 402, 403, 404],
]

for i in apart:
    print('NewsPaper ', end=' ')
    for j in i:
        print(j, end=' ')
    print('\n')

print('\n==================================================\n')