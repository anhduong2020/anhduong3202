# 작업 순서
# 1.1. 문자열을 입력
# 1.2. 문자열을  split() 해서 array 리스트로 만든다.
# 2. 반복문을 사용하여 array 리스틀르 루프를 돌면서 딕셔너리 table에 찾는다.
# 3. 찾았다면 바꾼다 .replace()
# 4. 문자열 메서드 join()을 사용하여 출력한다.

table = {"B4": "Before",
         "TX": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have A Nice Day"}

str = input("문자열을 입력하세요: ")
arr = str.split(" ")  # TX, Mr., Park!

result = ""
# for i in range(0, len(arr), 1):

for i in arr:
    value = table.get(i)
    if value == None:
        result = result + i + " "
    else:
        result = result + value + " "

print(result)
