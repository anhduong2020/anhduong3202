
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

class Counter:
    def __init__(self):
        self.__count = 0

    def reset(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def getCount(self):
        return self.__count

    def setCount(self):
        self.increment()


def main():
    instance1 = Counter()
    print(instance1.__str__())

    instance1.increment()
    instance1.increment()

    curval = instance1.getCount()
    print("Curval", curval)
    print(instance1.__str__())


if __name__ == "__main__":
    main()
