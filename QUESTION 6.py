def divide_numbers(numerator, denominator):
    try:
        # Attempt to divide the numbers
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")


# Example usage:
print(divide_numbers(10, 2))  # Expected output: 5.0
print(divide_numbers(10, 0))  # Expected output: Error: Cannot divide by zero.
print(divide_numbers(10, 'a'))  # Expected output: Error: Invalid input types. Please provide numbers.
