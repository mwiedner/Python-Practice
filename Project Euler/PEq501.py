def f(n):
    eights_list = []
    for i in range(3, n):
        divisor_counter = []
        for j in range(1, i+1):
            if i % j == 0:
                divisor_counter.append(j)
            if len(divisor_counter) == 8 and j == i:
                print(divisor_counter)
                eights_list.append(i)
                break
    print(eights_list)
    return len(eights_list)
print(f(10**2))