
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오

import os.path

readfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/proverbs.txt", "r", encoding=("UTF-8"))
outfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/output.txt", "w", encoding=("UTF-8"))

line = readfile.readline()
while line != "":
    print(line, end="")
    outfile.write(line)
    line = readfile.readline()

readfile.close()
outfile.close()
