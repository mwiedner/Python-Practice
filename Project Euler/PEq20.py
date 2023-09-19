def get_factorial(n):
    if (n == 1):
        return n
    else:
        i = n
        result = n
        while (i > 1):
            i = n - 1
            result = result * (i)
            n-=1
        return result
    
# Function to get sum of digits 
def get_sum(n):
     
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
    
print (get_sum(2**1000))