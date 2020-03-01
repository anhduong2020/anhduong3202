# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 4명이상
# 3. 학생 성적 입력 받기. 몇 번 입력 받아야 하는가?
# 4. 3번 학생의 성적을 100점으로 바꾸시오.
# 5. list에서 마지막 학생 삭제.
# 6. list에서 첫번째 값을 출력하시오.
# 7. 평균을 구하고 출력.
Stugrad = []

n = input("학생수를 입력하시오:")
n = int(n)

if n >= 4:
    for i in range(0, n, 1):
        j = input(" 성적을 입력하시오:")
        j = int(j)
        Stugrad.append(j)
    print("합계는: ", sum(Stugrad))

    # 평균값을 출력한다.
    arg = sum(Stugrad)/len(Stugrad)
    str = "성적의 평균은 %d 입니다." % arg
    print(str)
else:
    print("학생수는 최소 4이상이다")
