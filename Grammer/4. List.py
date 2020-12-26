print('==================================================\n')#

# 리스트

daishin = [9130, 9150, 9150, 9300, 9400]

print(daishin[0])       # 리스트의 첫번쨰는 0으로 시작
print(daishin[1])
print(daishin[-1])      # 리스트의 마지막부터는 -1로 시작

# 리스트 슬라이싱

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대자동차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']

print('시가총액 5위 :',kospi_top10[4])
print('시가총액 1 - 5 :',kospi_top10[:5])
print('시가총액 10위 :',kospi_top10[-1])

# 리스트 데이터 삽입

kospi_top10.append('SK텔레콤')         # append 는 맨 뒤에 데이터가 추가 됨
print(kospi_top10)

kospi_top10.insert(3, 'SK텔레콤')      # insert 는 insert(위치, 데이터) 로 데이터를 삽입
print(kospi_top10)

# 리스트 데이터 삭제

del kospi_top10[-1]                  # del 은 데이터 삭제 함수임
print(kospi_top10)

print('==================================================\n')

# 튜플

t = ('Samsung', 'LG', 'SK')
print(t)
print(len(t))
print(t[1])
print(t[0])
print(t[0:2])

print('==================================================\n')

# 딕셔너리

cur_price = {}

# 딕셔너리 추가

cur_price['daeshin'] = 30000
print(cur_price)
cur_price['KaKao'] = 80000
print(cur_price)
print(cur_price['daeshin'])
cur_price['Naver'] = 800000

# 딕셔너리 삭제

# del cur_price['daeshin']
# print(cur_price)

# 딕셔너리 키 값

print(cur_price.keys())
print(list(cur_price.keys()))       # 딕셔너리 키 값을 리스트로 변경
print(list(cur_price.values()))     # 딕셔너리 값을 리스트로 변경

# 딕셔너리 참 거짓

print('Samsung' in cur_price.keys())        # 삼성이 딕셔너리 안에 있는지 참 거짓 분별
print('Naver' in cur_price.keys())          # 네이버는 딕셔너리 안에 있으니 True


