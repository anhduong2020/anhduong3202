
# 파일을 연다.
openfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/data.csv", "r", encoding=("UTF-8"))
# 파일 안의 각 줄을 처리한다.
for line in openfile.readlines():
    line = line.strip()
    parts = line.split(",")
    for part in parts:
        print(" ", part)

openfile.close()

# 공백 문자를 없앤다.

# 줄을 출력한다.

# 줄을 쉼표로 분리한다.

# 각 줄의 필드를 출력한다.
