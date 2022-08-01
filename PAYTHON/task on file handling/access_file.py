f = open("myfile.txt", "w")
f.writelines(["\nThis line is for checking writeline method..."])
f.close()

# Take the filename to check
filename = input("myfile.txt\n")
# Open the file for the first time using open() function
fileHandler = open("myfile.txt", "r")
# Try to open the file same file again
try:
    with open("myfile.txt", "r") as file:
        # Print the success message
        print("File has opened for reading.")
# Raise error if the file is opened before
except IOError:
    print("File has opened already.")