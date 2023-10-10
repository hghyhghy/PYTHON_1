# use of map function in python


# first of all creating a function


# def ofcube(x):
#     return x * x * x


# print(ofcube(3))


# now doing the same operation of cubing a list elements byy uisng map function

# creating a list

l = [1, 2, 3, 4, 3, 4, 5, 2]

# newList = list(map(ofcube, l))

# print(newList)

# use of filter function in python

# iit is used to  filetr a list and return elements which has passed the filteration

# creating a definition


def filterizaion(a):
    return a > 3


newl1 = list(filter(filterizaion, l))

# printing the filtered output

print(newl1)

# now by using a lamda function


list1=list(map(lambda x:x*x*x,l))


print(list1)