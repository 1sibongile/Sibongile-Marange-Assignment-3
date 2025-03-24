import random

# Function to generate a list of 10 random integers between 1 and 100
def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(10)]

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Main part of the program
random_numbers = generate_random_numbers()  # Generate the random numbers
average = calculate_average(random_numbers)  # Calculate the average

# Print the results
print("Random Numbers:", random_numbers)
print("Average:", average)
