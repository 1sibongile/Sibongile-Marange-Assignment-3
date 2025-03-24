def calculate_average(*args):
    """
    Calculate the average of a given set of numbers.

    Parameters:
    *args (int or float): A variable number of numeric arguments.

    Returns:
    float: The average of the numbers passed as arguments.
           Returns 0 if no numbers are provided.
    """
    if len(args) == 0:
        return 0  # If no numbers are provided, return 0
    return sum(args) / len(args)  # Sum the numbers and divide by the number of arguments

# Example usage:
print(calculate_average(10, 20, 30))  # Output: 20.0
print(calculate_average(5, 15, 25, 35))  # Output: 20.0
print(calculate_average())  # Output: 0
