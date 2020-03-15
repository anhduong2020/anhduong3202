# phones.txt 파일에 아래의 2줄 쓰고 저장하시오.
# 최무선  010-1111-2222")
# 정중부  010-2222-3333

import os.path

outfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt", "a", encoding="UTF-8")

outfile.write("최무선 010-1111-2222\n")
outfile.write("정중부 010-2222-3333\n")

outfile.close()
