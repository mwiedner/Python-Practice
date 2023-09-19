import math

maxVal = math.ceil(1929394959697989990**0.5)
minVal = math.floor(1020304050607080900**0.5)

def theTest(n):
    strn = str(n)

    i = 0
    z = 0
    while i < 19:
        if strn[i] != z + 1:
            break
            return False
        i+=2
        z+=1
    return True


checking = True
i = maxVal
while checking:
    i-=10
    print(i**2)
    checking = theTest(i**2)
print("Finished:")
print(i)