
import os.path

outfile = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt", "w", encoding="UTF-8")

if os.path.isfile("C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt"):
    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5978\n")
    outfile.write("김영희 010-1264-5678\n")

else:
    print("동일한 이름의 파일이 이미 존재합니다.")
outfile.close()
