NumList = []

for i in range(1, 11, 1):
    n = input()
    n = int(n)
    NumList.append(n)
#print("INPUT:", NumList)
print("리스트 정렬 전:", NumList)
print("리스트 정렬 후:", sorted(NumList))
print("최소값:", min(NumList))
print("최대값:", max(NumList))
