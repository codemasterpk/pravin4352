# write a python program to sort (ascending and descending) a dictionary by value.

# you can take the input as integers also this'
# will work for that also for eg:{1:2,3:4,4:3,2:1,0:0}
y = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

l = list(y.items())  # convet the given dict. into list
# In Python Dictionary, items() method is used to return the list
# with all dictionary keys with values.
l.sort()  # sort the list
print('Ascending order is', l)  # this print the sorted list

l = list(y.items())
l.sort(reverse=True)  # sort in reverse order
print('Descending order is', l)

dict = dict(l)  # convert the list in dictionary

print("Dictionary", dict)  # the desired output