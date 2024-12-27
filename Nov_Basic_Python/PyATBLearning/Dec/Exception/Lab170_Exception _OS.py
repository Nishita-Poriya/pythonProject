import os
print(os.getcwd())
# return current working directory


# List files in the current directoryfiles=os.listdir('/Users/kaushal07/pythonProject/Nov_Basic_Python/PyATBLearning/Dec/Exception')
print(f"Files in directory :{files}")

# Create a new directory
#os.mkdir('Test2')

# Check if a file exists
file_exist=os.path.exists("nishita.txt")
print(file_exist)

print(os.name) # posix == mac, nt - windows