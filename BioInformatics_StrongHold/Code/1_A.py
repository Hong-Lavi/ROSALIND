# Example of File I/O in Python
"""
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("File I/O in Python is simple!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")

# Reading the updated file
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated File Content:")
    print(updated_content)

# Note: This code will create a file named 'example.txt' in the current directory.
"""
# Real code
with open("Example_Data/rosalind_dna.txt", "r") as file:
    string = file.read().strip()

def CountingDNA(string):
    count={"A":0,"C":0,"G":0,"T":0}
    for i in string:
        count[i]+=1
    return count
result=CountingDNA(string)

print(result["A"],result["C"],result["G"],result["T"])


