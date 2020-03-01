# 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.
# e. 정수리스트의 합계, 평균, 최대값 그리고 최소값을 구하시오.


def main():

    temp = "74 874 9883 73 9 73646 774"

    arr1 = temp.strip().split(" ")

    arr2 = []
    for n in arr1:
        n = int(n)
        arr2.append(n)
    print(arr2)

    print("오름차순 정렬하기:", sorted(arr2))
    print("최소값은: ", min(arr2))
    print("최대값은: ", max(arr2))
    print("합계: ", sum(arr2))
    print("평균은: ", sum(arr2)/len(arr2))


main()
