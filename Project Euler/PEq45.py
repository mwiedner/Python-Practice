def penta(p):
    # p = n(3n-1)/2
    # 0 = 1.5n^2 - 0.5n - p

    absurdity = quadratic(1.5, -0.5, (-1 * p))
    ab1 = absurdity

    print(p)
    print(ab1)
    print(" ")

    if (ab1 % 1 == 0):
        return True
    else:
        return False
    
def hexa(p):
    # p = n(2n-1)
    # 0 = 2n^2 - n - p

    absurdity = quadratic(2, -1, (-1 * p))
    ab1 = absurdity

    if (ab1 % 1 == 0):
        return True
    else:
        return False
    
def quadratic(a, b, c):
    result = (((-1*b) + (b*b - 4 * a * c)**(0.5)) / (2*a))
    return result

i = 286
looping = True

while looping:

    triangle = i * (i + 1) / 2
    if penta(triangle) and hexa(triangle):
        looping = False
    i+=1
print("And the result is: " + str(triangle))