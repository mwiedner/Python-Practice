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

strG = str(1020304050607080900)

def newTest(n):
    root = n ** 0.5
    if root % 1 == 0:
        return True
    else:
        return False

while something:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    strG[i] = j


checking = True
i = maxVal
while checking:
    i-=10
    print(i**2)
    checking = theTest(i**2)
print("Finished:")
print(i)