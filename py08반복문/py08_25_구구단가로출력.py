# 2단부타 19단까지 1씩 증가시키면서
# 1부터 9까지 1씩 증가시키면서
# 구구단을 출력하시오. 2*1=2 2*2=4

for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str = "%2s*%s=%3s" % (i, j, i*j)
        print(str, end=" ")
    print()


for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str = "%2s*%s=%3s" % (i, j, i*j)
        if j == 9:
            print(str, end=".")
        else:
            print(str, end=",")
    print()
