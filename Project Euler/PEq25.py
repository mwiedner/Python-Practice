f = 0
f1 = 0
f2 = 1
i = 1

while (f2 % 10**1000 < 10**999):
    i+=1
    f = f1 + f2
    f1 = f2
    f2 = f

print(f)
print(i)