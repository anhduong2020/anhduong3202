

#########################
# readline() 파일에서 한 줄씩 읽기
print("readline() 파일에서 한 줄씩 읽기")
prf = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt", "r", encoding=("UTF-8"))
s = prf.readline()
print(s, end="")
s = prf.readline()
print(s, end="")
s = prf.readline()
print(s, end="")
prf.close()

#########################
##
print("반복문으로 파일에서 읽어서 모니터에 출력하기")
prf = open(
    "C:/Python 20200209/Python기초20200103/st01.Python기초/py31파일처리/file/phones.txt", "r", encoding=("UTF-8"))
line = prf.readline()
while line != "":
    print(s, end="")
    line = prf.readline()
prf.close()
#########################
##
