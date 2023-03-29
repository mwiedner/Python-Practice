def is_palindrome(s):
    """
    This function checks if a given string is a palindrome or not.
    """
    # Remove all whitespace and convert to lowercase
    s = s.replace(' ', '').lower()
    # Check if the string is the same as its reverse
    return s == s[::-1]

# Example usage
string1 = "A man a plan a canal Panama"
string2 = "Hello World"
print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: False


j = 999*999
m = 0
looping = 1

while (looping):

    if is_palindrome(str(j)):   
        m = 999   
        while (j % m != 0):
            m-=1
        if (m > 100 and m < 1000):
            if (j / m < 1000):
                looping = 0
    j-=1

print(j+1)
print(m)

print((j+1) / m)