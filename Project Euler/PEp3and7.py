goal = 600851475143 

def is_prime(s):
    """
    This function checks if a int is prime.
    """
    i = s - 1

    while (i > 1):
        if s % i == 0:
            return 0
        else:
            i-=1
    return 1

looping = 1
n = 2
while (looping):
    if (is_prime(n)):
        print("n: " + str(n))
        print("Goal: " + str(goal))
        if (goal % n == 0):
            goal = goal / n
    elif (n >= goal):
        looping = 0
    n+=1

j = 10001
p = 3

while (j > 1):
    if (is_prime(p)):
        j-=1
    p+=2
    print(j)

print(goal)

print(p)
print(p)
print(p)