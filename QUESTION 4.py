# List of names to write to the file
names = ["Sibongile", "Precious", "Kenny", "Cute", "Thembi"]

# Writing names to names.txt
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")  # Write each name on a new line

# Reading names from names.txt and printing them
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes any trailing newlines
