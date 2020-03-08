
Eldic = {}

Eldic["one"] = "하나"
Eldic["two"] = "둘"
Eldic["three"] = "셋"
print(Eldic)
test = input("찾고 싶은 단어를 입력하시오:")
print(Eldic.get(test, "없음"))
