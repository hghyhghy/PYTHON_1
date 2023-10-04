# creating a list


marks = [3, 5, 6, 8, 9, 11, "subham", 67, 89, 56, 8]

# printing the list

print(marks)

print(type(marks))

# printing the number each by each

print(marks[0])

print(marks[1])

print(marks[2])


# accessing the elements by negative indexing


print(len(marks) - 1)

# checking wheather a particular number is present in the list or  not

if 8 in marks:
    print("Yes Present!")

else:
    print("No Not Present")

if "su" in "subham":
    print("yes")


print(marks[0:])

# using jump index

print(marks[0:5:2])
