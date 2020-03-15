
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기
import math


class Circle(object):
    def __init__(self, radius=0):
        self.radius = radius

    def calArea(self):
        resulf = math.pi * self.radius**2
        return resulf

    def calcCircum(self):
        resulf = 2*math.pi*self.radius
        return resulf


def main():
    c1 = Circle(10)
    print("원 반지름=", c1.radius)
    tmp = "원의 넓이는 %2.4f,둘레는 %2.4f 이다." % (c1.calArea(), c1.calcCircum())
    print(tmp)


# main()  # main 함수 호출
if __name__ == "__main__":
    main()
