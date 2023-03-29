numbers = []
while True:
    num_input = input("Enter a number (or 'done' to finish): ")
    if num_input == 'done':
        break
    try:
        num = float(num_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if len(numbers) > 0:
    min = numbers[0]
    max = numbers[0]
    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num

    print("Maximum:", max)
    print("Minimum:", min)
else:
    print("No numbers were entered.")
