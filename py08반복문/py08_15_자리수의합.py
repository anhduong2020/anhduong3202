x = input("정수를 입력하세요>>")

a = len(x)
print(a)

sum = 0
for i in range(1, a+1, 1):
    sum = sum + i
str = "%s,자리수의 합은 %s입니다" % (x, sum)
print(str)


#정수 = "1234"
# 1 == 정수[0]
# 2 == 정수[1]
# 3 == 정수[2]
# 4 == 정수[3]

# 작업 순서
# 1. 정수열 정수의 길이를 구한다. len 함수 사용
# 2. 0부터 길이-1 까지 1씩 증가시키면서
# 2-1. 문자 한개를 꺼내 정수로 변환
# 2-2. sum + 정수을 구한다.
num = input("정수 입력>>")
length = len(num)
sum = 0
for i in range(0, length, 1):
    x = int(num[i])
    sum = sum + x
str = "%s,자리수의 합은 %s입니다" % (num, sum)
print(str)
