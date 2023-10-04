# creating tuple

tuple = ("Subham", "Shreyoshi", "Shrestha")

# printing the type of it

print(type(tuple))

print(tuple)


# accessing the elements of the tuple

print(tuple[0])

print(tuple[1])

print(tuple[2])
# or this method can be used

print(tuple[0 : len(tuple)])

# using a if else loop to find a element

if "Subham" in tuple:
    print("Yes subham is present in the list ")

else:
    print("No we could not find anything")

# tuple slicing

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m1 = m[0 : len(m) - 1]

print("The first tuple is ", m)

print("The new sliced tuple is ", m1)
