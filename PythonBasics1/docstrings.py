# docstrings are not comments they are usd in function to tell about the function

# creating a function


def ofSquare(n):
    """This is a function where it takes input from user and returns the squared version of that"""

    print(n**2)


# num = int(input("Please enter the value:"))

# temp = ofSquare(num)

# print("The squared value is", temp)

temp = ofSquare(int(input("Enter the Number")))

# print(temp)

# printing the doc string

print(ofSquare.__doc__)
