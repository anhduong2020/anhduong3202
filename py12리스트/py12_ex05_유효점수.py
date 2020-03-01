
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.
# step3. 심사 위원의 점수 입력 받아서 list에 저장.
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지
# step5. 평균을 구하는 메서드 만들기.
#     평균값 = (double)sum / ( list.size() - 2 )
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.

ArrayList1 = []

n = input("심사 위원의 수를 입력하시오:")
n = int(n)
for i in range(0, n, 1):
    j = input("심사 위원의 점수 입력:")
    j = int(j)
    ArrayList1.append(j)

ArrayList1.sort()
ArrayList1.pop(0)
ArrayList1.pop(len(ArrayList1)-1)
print("유효점수: ", ArrayList1)

print("합계: ", sum(ArrayList1))


arg = sum(ArrayList1)/len(ArrayList1)

# 평균값을 출력한다.
str = "성적의 평균은 %0.2f 입니다." % arg
print(str)
