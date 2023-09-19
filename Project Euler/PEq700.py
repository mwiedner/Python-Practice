pa = 1504170715041707
pb = 4503599627370517
EC = 1 # 1504170715041707
ECm = 1504170715041707
i = 1
sum = EC

final = 111054189

while EC != final:
    calculation = (pa * i) % pb
    if calculation > EC:
        EC = calculation
        sum += EC
        print(EC)
    i+=1
print("fin")
print(sum)