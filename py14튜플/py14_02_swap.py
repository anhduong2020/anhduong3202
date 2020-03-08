
# swap이란? 변수의 값을 바꾸는 코딩 기법

# 1. 외팔이 기법
# 2. 튜플을 사용하는 방법, 파이썬에서만 가능
# hoan doi gia tri cua bien
x = 2
y = 3

tmp = x
x = y
y = tmp

print("x = ", x, "y= ", y)
(x, y) = (y, x)  # 튜플을 이용하여 swap 하는 방법
print("x = ", x, "y= ", y)
