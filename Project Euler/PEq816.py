s0 = 590797
k = 14

def rng(sn):
    return (sn**2) % 50515093

def pointx(n):
    sn = s0
    Tn = n * 2
    while (n != Tn):
        sn = rng(sn)
        n+=1
    return sn

def pointy(n):
    return rng(pointx(n))

def distance(x1, y1, x2, y2):
    return (((x2-x1)**2) + ((y2 - y1)**2))**0.5

shaw = 1000000
x = 0
while (x < k):
    y = 0
    while (y < k):
        big = distance(pointx(x), pointy(x), pointx(y), pointy(y))
        print(x)
        if (big < shaw) and (big != 0):
            shaw = big
        y+=1
    x+=1

print(shaw)