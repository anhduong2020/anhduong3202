# 1���� 100 ������ ���? �Ҽ��� ã�� �ڵ带 �ۼ��Ͻÿ�.


def isprime(n1, n2):

    for i in range(n1, n2, 1):
        if (n1 % i == 0):
            return False
    return True


#n = int(input("������ �Է��Ͻÿ�: "))
# print(isprime(n))

def myinput(mesg):
    n1 = input(mesg)
    n1 = int(n1)
    return n1


def main():
    # �Է� ó��
    n1 = myinput("ù��° ������ �Է��Ͻÿ�:")
    n2 = myinput("�ι�° ������ �Է��Ͻÿ�:")
    if n1 > n2:
     # ���� �ٲٰ�
        temp = n1
        n1 = n2
        n2 = temp
    else:
        pass

    val = isprime(n1, n2)
    # print(val)

    if val == True:
        print("?????: %s" % n1)


main()
