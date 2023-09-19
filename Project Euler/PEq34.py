import math

def getDigits(n):
    strN = str(n)
    length = len(strN)
    list = []

    i = 0
    while i < length:
        list.append(int(strN[i]))
        i+=1
    return list

k = 100
while k < 10000000:
    list = getDigits(k)
    length = len(str(k))
    sum = 0
    i = 0
    while i < length:
        sum+=math.factorial(list[i])
        i+=1

    if sum == k:
        print(k)
    k+=1
print("fin")