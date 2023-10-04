# creating a list in python

l = [1, 2, 3, 4]

# printing the list

print(l)

# using append function to enter an element to the last

l.append(5)

print(l)

# now methods to sort the list elements in ascending order


l1 = [34, 4, 49, 1, 10, 99]

print(l1)

print("After sorting the list will be ")

l1.sort()

print(l1)

# now printing the list in descending order

l1.sort(reverse=True)

print(l1)

# printing an index of the list

print(l1.index(34))

# now printing the ocurance of an element in the list

l2 = [2, 3, 4, 5, 2]

print(l2.count(2))

# entering a new element in the list using insert method

l2.insert(0, 89)

print(l2)

# using extend method

# creating a new list

m = [999, 1999, 2999]

print(l2)

print("After using the extend method the list l2 will be ")

l2.extend(m)

print(l2)
