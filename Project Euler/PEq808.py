# print(169+961 +12769+96721+1042441+1062961 +1216609 +1442401 +1692601 +9066121 +121066009 +900660121 +12148668841 +12367886521 +12568876321 +14886684121 +1000422044521 +1002007006009 +1020506060401 +1040606050201 +1210684296721 +1212427816609 +1212665666521 +1214648656321 +1234367662441 +1236568464121 +1254402240001 +1256665662121 +1276924860121 +1442667634321 +9006007002001 +9066187242121 +100042424498641 +100222143232201 +100240164024001 +100402824854641 +100420461042001 +102012282612769 +102014060240401 +102232341222001 +104042060410201 +121002486012769 +121264386264121 +121462683462121 +123212686214641 +146412686212321 +146458428204001 +146894424240001 +967210684200121 +967216282210201 )

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def reverse(num):
    """
    Reverse the digits of an integer.
    """
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    return reversed_num

num = 1
revCount = 0
sum = 0
while (revCount < 50):
    if is_prime(num):
        revy = reverse(num**2)
        if (is_prime(revy**0.5) and (revy**0.5 % 1 == 0) and revy != num**2):
            print("Prime: " + str(num) + " SQRT: " + str(num**2) + " Reverse: " + str(revy) + " SQRT: " + str(revy**0.5))
            revCount+=1
            print(revCount)
            sum+=num**2
    num += 2

print(str(sum) + "WOOOOO!")