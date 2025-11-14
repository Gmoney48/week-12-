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
########################################################
# list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - re moves and returns an item at a given index
#       (default is the last item)
# .remove() - removes the first occurrence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list 
#######################################################

# why is a list more useful than a variable?
# a list can hold mutiple values
# while a variable can only hold one value at a time
cakes = ['chocolate','vanilla','red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0])
# access the last item
# print(cakes{-1})
# want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
# add a new cake to the end of the list 
cakes.append('lemon')
print(cakes)
cakes[1] = 'chocolate'
print(cakes)
# remove the last cake
cakes.pop()
print(cakes)
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)
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
favorite_food = ['pizza', 'wings','tacos','burger','chicken' ]
# # Print the second and last item.
print(favorite_food[1])
print(favorite_food[-1])
# Add a new item using .append().
favorite_food.append('pasta')
# Remove the first item using .pop(0).
favorite_food.pop(0)
print(favorite_food)
# Reverse your list using .reverse().
favorite_food.reverse()
print(favorite_food)

# sets = {1, 2, 3}
# sets are unordered collections of unique items 
# sets do not support indexing or slicing 
# sets are mutable, meaning you can add or remove items
# sets are created using curly braces {}
my_set = (1, 2, 3, 4, 5)
print(my_set)
print(type(my_set))
# add an item to the set
my_set.add(6)
print(my_set)
# removes an item from the set
my_set.remove(3)
print(my_set)

# check if an item is in the set
print(4 in my_set) #true
print(3 in my_set) #false
# tuples are ordered collections of items
# typles are immutable, meaning you cannot modify them after creating
# tuples are created using parenthesis ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple{1:4})
# try to modify the tuple (will raise an error)