# A program to write a function that displays a String repeatedly

def repeatCharacters(n,string):
    new_string = ""
    for char in string:
        new_string = new_string + char*n
    return new_string

print(repeatCharacters(5,"string"))