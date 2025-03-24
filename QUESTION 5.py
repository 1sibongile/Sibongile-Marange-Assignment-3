# Sample list of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40, 50]

# Using map and lambda to convert Celsius to Fahrenheit
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print the converted list
print(fahrenheit_temperatures)
