import math

dimension = 1001
sum = 0
iterStop = math.ceil(dimension / 2)

def cornerCalc(d):
    d2 = d**2
    print("cC Called with " + str(d))
    if(d == 1):
        return 1
    else:
        return d2 + (d2 - (d-1)) + (d2 - (d-1) - (d-1)) + (d2 - (d-1) - (d-1) - (d-1))


while(iterStop > 0):

    sum += cornerCalc(dimension)


    dimension-=2
    iterStop-=1

print(sum)