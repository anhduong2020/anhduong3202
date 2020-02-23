# 중첩 for문

for a in range(1, 11, 1):
    for b in range(1, 11, 1):
        print("*", end="")
    print()
print("----------------------")

# tang dan
for a in range(1, 11, 1):
    for b in range(1, a, 1):
        print("*", end="")
    print()

print("----------------")
# giam dan
for a in range(1, 11, 1):
    print("")
    for b in range(1, a+1, 1):
        print(" ", end="")
    for b in range(a+1, 11, 1):
        print("*", end="")
print()
