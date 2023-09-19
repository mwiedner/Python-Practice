def collatz(n):
    looping = 1
    i = 0
    j = n
    while (looping):
        i+=1
        if (j==1):
            looping = 0
        elif (j % 2 == 1):
            j = (3*j + 1)
        elif (j % 2 == 0):
            j = (j/2)
    return i

i = 1
bigboy = 1
imp = 1
while (i < 1000000):
    z = collatz(i)
    if (bigboy < z):
        imp = i
        bigboy = z
    i+=2
    print(i)
print(imp)