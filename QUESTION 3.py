def get_valid_number():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)  # Try to convert input to a float
            print(f"You entered a valid number: {number}")
            break  # Exit the loop once the input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to prompt user for input
get_valid_number()
