# ./file/proverbs.txt 파일 열기

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.
import os.path
filename = input("파일명을 입력하세요: ").strip()

infile = open("C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/" +
              str(filename), "r", encoding=("UTF-8"))

dic = {}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.

for line in infile:
    for char in line.strip():
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
print(dic)
infile.close()
