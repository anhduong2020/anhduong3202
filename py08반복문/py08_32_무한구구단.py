

print("종료하려면 음수을 입력하시오 ")
while True:
    x = input("시작 단수를 입력하세요>>")  # 문자열
    x = int(x)  # 문자열을 정수로 바꾸

    y = input("종료 단수를 입력하세요>>")
    y = int(y)

    if x > y:
        temp = x
        x = y
        y = temp

    if x <= 0 or y <= 0:
        break

    for i in range(x, y+1, 1):
        for j in range(1, 10, 1):
            str = "%2s*%s=%3s" % (i, j, i*j)
            if j == 9:
                print(str, end=".")
            else:
                print(str, end=",")
        print()
