""" 
This module provides a generator to read lines from a CSV file one by one.
"""


import csv

# Generator function to yield lines one by one
def read_lines(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            yield row  # Yield each row one at a time

# Function to print the next line each time it's called
def print_next_line():
    if not hasattr(print_next_line, "csv_gen"):
        print_next_line.csv_gen = read_lines('random_lines.csv')  # Initialize the generator only once
    try:
        row = next(print_next_line.csv_gen)  # Get the next line
        print(row)  # Print the row
    except StopIteration:
        print("End of file reached.")

# Example usage
print_next_line()  # First call: prints the first line
print_next_line()  # Second call: prints the second line
print_next_line()  # Third call: prints the third line
print_next_line()  # Third call: prints the third line
