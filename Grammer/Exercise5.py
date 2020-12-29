print('\n==================================================\n')

# 문제 1
# 다음 조건을 만족하는 Pointer 클래스를 작성하세요.

class Pointer:

    def __init__(self, x, y):
        print("x, y 좌표를 받았습니다.")
        self.x = x
        self.y = y

    def setx(self, x):
        print("x 좌표를 받았습니다.")

    def sety(self, y):
        print("y 좌표를 받았습니다.")

    def get(self):
        print("현재 좌표는 x : %d, y : %d 입니다" % (self.x, self.y))

        getxy = (self.x, self.y)

        return getxy

    def move(self, dx, dy):
        print("현재 좌표에서 %d, %d 만큼 이동합니다." % (dx, dy))
        self.x += dx
        self.y += dy
        print("현재 좌표는 x : %d, y : %d 입니다" % (self.x, self.y))

print('\n==================================================\n')

# 문제 2
# 문제 1 에서 생성한 Pointer 클래스에 대한 인스턴스를 생성한 후 4개의 메서드를 사용하는 코드를 작성하세요.

pointer = Pointer(1, 2)
pointer.get()
pointer.move(3, 3)

print('\n==================================================\n')

# 문제 3
# 아래의 Stock 클래스에 대해 2개의 인스턴스를 생성했을 때 클래스와 a와 b 인스턴스의 네임스페이스를 그려보세요.

class Stock:
    market = "kospi"

a = Stock()
b = Stock()

print('\n==================================================\n')

# 문제 4
# 문제 3의 코드에서 추가로 아래와 같은 코드를 수행했을 때 '???' 로 표시된 부분의 결괏값을 적어보세요.

print(a.market)
print(b.market)
print(Stock.market)

a.market = "kosdaq"
b.market = "nasdaq"

print(a.market)
print(b.market)
print(Stock.market)

print('\n==================================================\n')