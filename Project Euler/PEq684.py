import math



def digitSum(n):
    if (n < 10):
        return n
    else:
        numNine = math.floor(n / 9)
        leadDigit = (n - (9 * numNine)) % 9

        result = leadDigit * (10**numNine)

        while (numNine > 0):
            numNine-=1
            result = (result + (9*(10**numNine)))
        return (result)

f = 0
f1 = 0
f2 = 1
sum = 0

i = 2
while i <= 90:
    print(i)
    
    f = f1 + f2
    f1 = f2
    f2 = f

    sum+=(digitSum(f2))
    i+=1

print("fin")
print(sum % 1000000007)