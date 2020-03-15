
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기
import Circle


def main():
    a = int(input("원반지름= "))
    c1 = Circle.Circle(a)

    tmp = "원의 넓이는 %2.4f\n둘레는 %2.4f 이다." % (c1.calArea(), c1.calcCircum())
    print(tmp)


# main()  # main 함수 호출
if __name__ == "__main__":
    main()
