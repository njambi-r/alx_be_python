# This script will prompt the user to enter a positive integer, 
# then use nested loops to print a square pattern of that 
# size made of asterisks (*).

# Prompt user for pattern size
pattern_size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
current_row = 0

# Draw the pattern
while current_row <= pattern_size:
    for i in range (1, pattern_size +1):
        print("*", end="")
    current_row += 1
    print()


