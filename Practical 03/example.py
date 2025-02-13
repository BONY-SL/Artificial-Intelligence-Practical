# print('apple' < 'banana')

# print(bool('A'))

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Slicing in Python

# List slicing in Python
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# Add/Change/Delete List Items

# Correcting mistake values in a list

odd = [2, 4, 3, 8]

# Change the 1st Item
odd[0] = 1
print(odd)

# Change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)

# Appending and Extending lists in Python
odd = [1, 3, 5]

print(odd)

odd.append(7)

print(odd)

odd.extend([9, 11, 13])
print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5])

print(["re"] * 3)


# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]
print(my_list)

# delete multiple items
del my_list[1:5]
print(my_list)

# delete the entire list
del my_list

# Error: List not defined
print(my_list)

# Example on Python list methods
my_list = [3, 8, 1, 6, 8, 8, 4]
# Add 'a' to the end
my_list.append('a')
print(my_list)

# Index of first occurrence of 8
print(my_list.index(8))
# Count of 8 in the list
print(my_list.count(8))

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)

rgb = ('red', 'green', 'blue')

print(rgb[0])
print(rgb[1])
print(rgb[2])

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
numbers = (3,)
print(type(numbers))
numbers = (3)
print(type(numbers))

tuple1 = ("abc", 34, True, 40, "male")
mytuple = ("apple", "banana", "cherry")
print(type(tuple1))
print(type(mytuple))

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

skills = {'Python programming', 'Databases', 'Software design'}

empty_set = {}

empty_set = set()

skills = set()

if not skills:
    print("Empty sets are falsy..")

ratings = {1, 2, 3, 4, 5}
size = len(ratings)

print(size)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

















































