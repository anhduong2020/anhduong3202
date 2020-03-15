
#########################
# 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
#########################

import os.path

outfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt", "w", encoding="UTF-8")

if os.path.isfile("C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt"):
    a = input("text1: ")
    outfile.write(a)
    print(a)

else:
    print("동일한 이름의 파일이 이미 존재합니다.")
outfile.close()
