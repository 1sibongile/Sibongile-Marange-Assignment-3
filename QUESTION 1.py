def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    try:
        user_input = int(input("Enter an integer: "))
        result = classify_number(user_input)
        print(f"The number is {result}.")
        break  # Exit loop once a valid integer is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer.")