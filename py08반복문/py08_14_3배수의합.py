i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum = sum + i
    i = i + 1  # i를 1씩 증가시키면서

str = "%s부터 %s사이의 3의 배수의 합계는 %s" % (1, 100, sum)
print(str)
print("while 문 종료")

sum1 = 0
for x in range(0, 101, 3):
    sum1 = sum1 + x
str = "%s부터 %s사이의 3의 배수의 합계는 %s" % (1, 100, sum1)
print(str)
print("for 문 종료")

sum1 = 0
for x in range(1, 101, 1):
    if x % 3 == 0:
        sum1 = sum1 + x

str = "%s부터 %s사이의 3의 배수의 합계는 %s" % (1, 100, sum1)
print(str)
print("for 문 종료")
