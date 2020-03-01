
NumArray = []

print("종료하려면 음수를 입력하시오")
while True:  # 무한 루프
    num = input("성적을 입력하시오: ")
    # 정수로 변환
    num = int(num)
    # 입력값이 음수이면 반복문을 종료.  break
    if num < 0:
        break
    NumArray.append(num)
# 평균값을 계산한다.
arg = sum(NumArray)/len(NumArray)

# 평균값을 출력한다.
str = "성적의 평균은 %s 입니다." % arg
print(str)
