# Python - Multiple except blocks with one try block example

try:
    # Creating a list in Python
    arr = [1, 2, 3, 4]

    # trying to access an invalid 5th index in a list, hence IndexError Exception
    print('value = ', arr[5])


# except block to catch Exception exception
except Exception as e:
    print('Exception exception caught - ', e)


# except block to catch IndexError exception
except IndexError as e:
    print('IndexError exception caught -', e)