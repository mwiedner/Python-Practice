import math

def l1s_count(n):
    if n % 9 == 0:
        return 4
    elif n % 8 == 0 or n % 7 == 0:
        return 5
    elif n % 6 == 0:
        return 3
    elif n % 5 == 0 or n % 4 == 0:
        return 4
    elif n % 3 == 0:
        return 5
    elif n % 2 == 0:
        return 3
    elif n % 10 == 0:
        return 0
    else:
        return 3
    
def l10s_count(n):
    z = get_ten(n)
    if z == 9:
        return 6
    elif z == 8:
        return 6
    elif z == 7:
        return 7
    elif z == 6:
        return 5
    elif z == 5:
        return 5
    elif z == 4:
        return 6
    elif z == 3:
        return 6
    elif z == 2:
        return 6
    elif z == 1:
        if n % 100 == 11:
            return 6
        elif n % 100 == 12:
            return 6
        elif n % 100 == 13:
            return 8
        elif n % 100 == 14:
            return 8
        elif n % 100 == 15:
            return 7
        elif n % 100 == 16:
            return 7
        elif n % 100 == 17:
            return 

def get_hund(n):
    return math.floor(n / 100)

def get_ten(n):
    return (math.floor(n / 10) % 10)

def get_one(n):
    return n % 10

print(get_ten(1))