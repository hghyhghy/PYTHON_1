# the use of reduce function in python

# importing reduce by by "From"  keyword


from functools import reduce

# creating a list

numbers = [1, 2, 3, 4, 5]

# creating a function which returns sum of two numbers


def ofsum(x, y):
    return x + y


temp = reduce(ofsum, numbers)

# printing  the reduced value


print(temp)

# now doing the same thing by using a lamda function

num1 = [2, 3, 4, 5, 6]

temp1 = reduce(lambda x, y: x + y, num1)

# printing the reduced list

print(temp1)
