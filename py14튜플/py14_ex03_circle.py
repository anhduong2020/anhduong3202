import math  # goi thu vien toan tu de lay so PI


def calCircle(r):
    area = math.pi*r*r
    cirum = 2 * math.pi*r
    return (area, cirum)


def main():
    str = input("원의 반지름을 입력하시오:")
    radius = float(str)
    (a, c) = calCircle(radius)
    tmp = "원의 넓이는 %2.4f,둘레는 %2.4f 이다." % (a, c)
    print(tmp)


# main()  # main 함수 호출
if __name__ == "__main__":
    main()
