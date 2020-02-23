# 무한 반복문은 조건식을 True로 하면 된다
# 로프 탈풀은 break를 사용하면돤다

sum = 0
count = 0
print("종료하려면 음수을 입력하시오 ")
while True:
    num = input("성적을 입력하시오: ")
    num = int(num)
    # 입력값이 음수이면 반복문을 종료하시오
    if num < 0:
        break

    count = count + 1
    # 합계를 출력한다
    sum = sum + num

# 평균을 출력한다
aver = sum/count

str = "성적의 평균은 %s 입니다 " % aver
print(str)
