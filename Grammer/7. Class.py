print('\n==================================================\n')

# 클래스

def print_business_card(name, phone, email):
    print("---------------------")
    print("Name  :    %s" % name)
    print("Phone :    %s" % phone)
    print("Email :    %s" % email)
    print("---------------------")

print_business_card('김성수', '010.7722.8123', 'nfl1ryxditimo12@gmail.com')

class BusinessCard:

    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print('--------------------')
        print('Name :', self.name)
        print('Email :', self.email)
        print('Addr :', self.addr)
        print('--------------------')

member1 = BusinessCard()
print(type(member1))

member1.set_info('Kimseongsu', 'nfl1ryxditimo12@gmail.com', 'Cheonan')
member1.print_info()

member2 = BusinessCard()

member2.set_info('Sonjieun', 'sju@naver.com', 'Baebang')
member2.print_info()

print('\n==================================================\n')

# 클래스 생성자

class MyClass:

    def __init__(self):
        print("객체가 생성되었습니다.")

inst1 = MyClass()

class Business:

    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print('--------------------')
        print('Name :', self.name)
        print('Email :', self.email)
        print('Address :', self.addr)
        print('--------------------')

seongsu = Business('김성수', 'singj1963@naver.com', 'Cheonan')
seongsu.print_info()

print('\n==================================================\n')

# self 이해하기

class Foo:
    def func1():
        print("function 1")

    def func2(self):
        print("function 2")


f = Foo()               # 변수를 인스턴스로 찍어내기
f.func2()               # func2() 메서드 호출
# f.func1()             # func1() 메서드는 매개변수가 없어서 오류

print(id(f))            # f의 메모리상 주소 확인
f.func2()

f2 = Foo()
print(id(f2))
f2.func2()

Foo.func1()             # 이렇게 클래스.메서드() 방식으로 사용하면 func1() 메서드 호출 가능

f3 = Foo()
print(id(f3))
Foo.func2(f3)

print('\n==================================================\n')

# 클래스 네임스페이스

class Stock:
    market = "kospi"

print(dir())
print(Stock.__dict__)
print(Stock.market)

s1 = Stock()
s2 = Stock()
print(id(s1), id(s2))
print(dir())

s1.market = "kosdaq"                # s1 인스턴스 변수의 네임스페이스 안에 {"market": "kosdaq"} 라고 저장
print(s1.__dict__)
print(s2.market)                    # s2 인스턴스 변수의 네임스페이스 안에 'market' 변수가 없어서 클래스 네임스페이스에서 찾음

print('\n==================================================\n')

# 클래스 변수와 인스턴스 변수

class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

kim = Account("kim")
lee = Account("lee")

print(kim.name)
print(kim.num_accounts)
print(Account.num_accounts)

print('\n==================================================\n')

# 클래스 상속

class Parent:

    def can_sing(self):
        print("Sing a song")

father = Parent()
father.can_sing()

class LuckyChild(Parent):
    pass

child1 = LuckyChild()
child1.can_sing()

class UnLuckyChild:

    def __init__(self):
        print("넌 아무것도 못받았구나ㅠㅠ")
child2 = UnLuckyChild()

class LuckyChild2(Parent):

    def can_dance(self):
        print("Shuffle Dance")

child3 = LuckyChild2()
child3.can_sing()
child3.can_dance()

print('\n==================================================\n')