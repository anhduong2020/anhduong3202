x = int(input("x = "))
y = int(input("y = "))
try:
    z = x/y
except ZeroDivisionError:
    print(" 0으로 나누는 예외")

print("%s/%s= %3s" % (x, y, z))

print("-----------------")

num1 = input("a = ")
num2 = input("b = ")

try:
    num1 = int(num1)
    num2 = int(num2)

    res = num1/num2
except ValueError as ex:
    print("ValueError", ex)  # 로그 파일에 저장하는 방식으로 수정 필요
except ZeroDivisionError as ex:
    print("ZeroDivisionError", ex)
