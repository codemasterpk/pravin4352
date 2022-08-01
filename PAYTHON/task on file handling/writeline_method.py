f = open("myfile.txt", "w")
f.writelines(["\nThis line is for checking writeline method..."])
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())