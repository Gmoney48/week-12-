# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Lists are part of the collections family in Python
# Examples:
my_list = [1, 2, 3, 4, 5]
# print{my_list}
print(len(my_list))
print(type(my_list))
print (my_list[0])
print(my_list[1:4])
print(my_list[1:])
print(my_list[-1:])
# reverse the list
print(my_list[::-1])
# modifying a list 
my_list.append(6) # adds 6 to the end of the list
print(my_list)
# add 7 and 8 to the list 
my_list.extend({7,8})
print(my_list)
my_list.extend({8,9})
print(my_list)
# remove the item at index 2
my_list.pop(2)
print(my_list)
# sort the list in ascending order
my_list.sort()
print(my_list)
# reverse the list
my_list.reverse()
print(my_list)
# remove a spexific value
my_list.remove(4)
print(my_list)
# remove the last item using negative index
my_list.remove(-1)
print(my_list)
# make list to 50
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
my_list.extend(new_list)
print(my_list)
newlist = list(range(12, 220))
print(newlist)
my_list.append(newlist)
print(my_list)
my_list.extend(newlist)
print(my_list)
every_third_number = my_list[::3]
print(every_third_number)
every_ten = my_list[::10]
print(every_ten)
# remove every third element
del my_list[::3]
print(len(my_list))
print(my_list)

# list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - re moves and returns an item at a given index
#       (default is the last item)
# .remove() - removes the first occurrence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list 

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
# favorite_food = ['pizza, wings,tacos,burger,chicken' ]
# # Print the second and last item.
# print(favorite_food[1:])
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.