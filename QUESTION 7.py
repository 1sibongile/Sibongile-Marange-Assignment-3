# Step 1: Define the custom exception class NegativeNumberError
class NegativeNumberError(Exception):
    """Custom exception raised when a number is negative."""
    def __init__(self, message="Negative number is not allowed"):
        self.message = message
        super().__init__(self.message)

# Step 2: Function to check if the number is positive or negative
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Error: {number} is a negative number.")
    return number
# Step 3: Demonstrate the usage in a try block
try:
    num = int(input("Enter a number: "))  # Get user input
    result = check_positive(num)  # Call the function to check if the number is positive
    print(f"The number is positive: {result}")
except NegativeNumberError as e:
    print(e)  # This will print the error message for a negative number
except ValueError:
    print("Invalid input! Please enter a valid number.")  # Handle non-numeric inputs
