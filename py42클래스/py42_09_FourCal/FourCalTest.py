
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기
import math


class FourCal:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def Add(self):
        resulf = self.__x + self.__y
        return resulf

    def Minus(self):
        resulf = self.__x - self.__y
        return resulf

    def Mul(self):
        resulf = self.__x * self.__y
        return resulf

    def Div(self):
        resulf = self.__x / self.__y
        return resulf


def main():
    a = int(input("첫번째 수= "))
    b = int(input("두번째 수= "))
    f1 = FourCal(a, b)
    print(f1.__str__())


if __name__ == "__main__":
    main()
