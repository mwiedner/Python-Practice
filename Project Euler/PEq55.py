def palTest(n):
    strN = str(n)
    rev = strN[::-1]
    
    if rev == strN:
        return True
    else:
        return False
    
total = 0
i = 0
k = 0
while k < 10000:
    i = 0
    boo = True
    temp = k
    while i < 50:
        
        strK = str(temp)
        rev = strK[::-1]

        sum = temp + int(rev)

        pal = palTest(sum)

        if pal:
            boo = False
            i = 50
        temp = sum
        i+=1

    if boo:
        total+=1
    k+=1
print(total)