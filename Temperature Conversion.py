far = float(input('Enter a temperature in Fahrenheit: '))

result = '{:.2f}'.format((far - 32) * 5/9)

print("The temperature in Celsius is " + result + " degrees Celsius.")