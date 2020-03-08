# 딕셔너리 선언하기 dic = {"key":겂}
dictionary = {
    "name": "망고",
    "type": "당",
    "ingredient": ["망고", "설탕", "소금", "치자"],
    "origin": "필리핀"
}
print(dictionary)

# 딕셔너리에서 Value 읽기
print(dictionary["name"])
print(dictionary["type"])
print(dictionary["ingredient"])
print(dictionary["origin"])


#  딕셔너리의 CRUD3Se
# dung tu dien khi chua gia tri khong trung


# 요소 추가 전에 내용을 출력해봅니다.

# 딕셔너리 추가 (them gia tri)
dictionary["head"] = "머리"
dictionary["body"] = "몸"
# 선택 연사자 [] 로 딕셔너리 읽기
# dictionary의 head 값을 출력하시오
print("head 값", dictionary["head"])
print("head 값", dictionary.get("head"))
# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# try ~ except를 추가하시오
try:
    dictionary["존재하지 않는 키"]  # KeyError
except KeyError as ex:
    print(ex)  # 화면에 에러 출력하고 드름 라인 실행


# U: 딕셔너리 수정
# name 값을 "8D 망고"로 수정하시오
print("name", dictionary["name"])
dictionary["name"] = "8D 망고"
print("name", dictionary["name"])

# 딕셔너리 삭제.
# 1. 연산자 방식 => del
# 2. 메서드 방식 => .pop("key"). 추천
# name, type key를 삭제
print("삭제 전", dictionary)
dictionary.pop("name")
dictionary.pop("type")
print("삭제 후", dictionary)
# 딕셔너리 키 존재 여부 확인 =>
# 방법1- .get() 를 사용하는 방법
# .get() 메서드 키가 존재하지 않는 경우에 None을 반환한다.


value = dictionary.get("존재하지 않는 키")  # value 값이 None이면 키가 없다는 의미다.
if value == None:
    print("키가 존재하지 않는다.")
else:
    print("카가 존재한다.")
    print(value)

# 방법 2 - in 연산자를 사용하는 방법
if "존재하지 않는 키" in dictionary:
    print("카가 존재한다.")
    print(dictionary["존재하지 않는 키"])
else:
    print("키가 존재하지 않는다.")

print()
# value = dictionary["존재하지 않는 키"]  # KeyError

# 키가 존재하지 않는 경우의 확인 방법 :  None 사용

# 출력합니다.

# S: 정렬, 딕셔너리는 정렬하는 방법이 없다
# 단, key 값만 정렬하는 것을 가능하다, value 값만 정렬하는 것을 가능하다.

# S : 검색. 특별하는 방법이 없다
# 선책연산자를 사용하면 바로 검색 되기 때문이다.
# key 만 열거.keys() 메서드 사용.
for key in dictionary.keys():
    print("keys>>", key)


# Value 만 열거.values() 메서드 사용.
for value in dictionary.values():
    print("values>>", value)

# key, value를 쌍으로 열거. items() 메서드 사용.
for item in dictionary.items():
    print("item>>", item)

# 딕셔너리 열거

# key 만 열거

# value 만 열거

# key, value를 쌍으로 열거
