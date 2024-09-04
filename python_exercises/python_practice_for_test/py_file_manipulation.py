# Function to write on a file
# If the file doesn't exist, it creates it
# the with statement handles the closing of the file even if an exception occurs

def writeOnFile(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

# example 1
# writeOnFile('test.txt', 'This is a test!\nSo is this...\nAnd this...\nAnd also this')

# In order to have the text be on a new line add the \n to the beginning of the text 

def appendToFile(filename, text):
    with open(filename, 'a') as file:
        file.write(text)

# # # example 2
# appendToFile('test.txt', '\nAnd this probably is too!')

def deleteLine(filename, line_to_delete):
    # Read all lines from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Open the file in write mode to overwrite it
    with open(filename, 'w') as file:
        for line in lines:
            # Write all lines except the one you want to delete
            if line.strip("\n") != line_to_delete:
                file.write(line)

# Example 3
# delete_line('test.txt', 'This is a test!')

def deleteLineByPosition(filename, line_number):
    # Read all lines from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Open the file in write mode to overwrite it
    with open(filename, 'w') as file:
        for i, line in enumerate(lines):
            # Write all lines except the one at the specified position
            if i != line_number - 1:  # line_number - 1 because list indices start at 0
                file.write(line)

# Example usage
# deleteLineByPosition('test.txt', 2)  # Deletes the 3rd line

# Copy contents of one file into another

def readAndCopy(originFile,destinationFile):
    with open(originFile, 'r') as file:
     lines = file.readlines()
    writeOnFile(destinationFile,''.join(lines))

