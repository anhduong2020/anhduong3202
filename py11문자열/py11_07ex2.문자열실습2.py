# -*- coding: utf-8 -*-


# 도전 2. 형변환. 문자열을 정수로 바꾸기.
# 문자열 "3"을 정수 3으로 바꾸시오. 구글 검색
# temp2 = "3"

# 도전 3. 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.
temp3 = "74 874 9883 73 9 73646 774"


# 문자열이 리스트로 바뀐다 chuyen tu chuoi thanh danh sach chuoi
array1 = temp3.split(" ")
print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

# Chuyen tu danh sach chuoi thanh danh sach so nguyen
array2 = []
for n in array1:
    n = int(n)
    array2.append(n)
print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]
