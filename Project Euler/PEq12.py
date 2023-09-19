def get_triangle(n):
    if (n % 2 == 0):
        return (n+1)*(n/2)
    else:
        return ((n)*((n-1)/2)) + n
    
factors = []
factors.append(1)
n = 100000

while (len(factors) < 500) :
    factors.clear()
    n += 1
    loopage = 1
    i = 1
    print("T number:" + str(n))
    while (loopage):
        z = get_triangle(n)
        if (z % i == 0):
            factors.append(i)
        elif i >= z:
            loopage = 0
        i += 1

print(factors)
print("And the result is!!!: " + str(n))