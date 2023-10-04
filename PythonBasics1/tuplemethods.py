# manipulating the tuple by those following steps

# note that tuples are immutable

# first of all we are creating a tuple

countries = (
    "India",
    "Australia",
    "Ne Zealand",
    "England",
    "North America",
    "Latin America",
)

print(countries)

# to perform any operation  we have to make it list


temp = list(countries)

print(temp)

# applying append operation to the list named temp

temp.append("Russia")

# importing new value at index 0

temp.insert(3, "Bangladesh")

print(temp)

# deleting an item from the list named temp

temp.pop()

print(temp)

# now making the list back to tuple

countries = tuple(temp)

print(countries)


# concatenating two tuples


t1 = (1, 2, 3, 4)

t2 = (5, 6, 7, 8)

t3 = t1 + t2

print(t3)

# printing the list of the concatenated tuple

print(len(t3))


