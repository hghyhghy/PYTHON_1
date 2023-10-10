# creating a function


def double(x):
    return x * 2


print(double(5))

# and now doing the same opeeration by using lamda function

double = lambda x: x * 2

print(double(6))

cube = lambda x: x * x * x

print(cube(5))


# printing the average by using lamda function

average = lambda x, y: (x + y) / 2

print(average(3, 5))


def isLeapyear(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(f"The year {y} is a leapyear")  # by using f string

    else:
        print(f"The year {y} is not a leapyear")  # by using f string


y = int(input("Enter the Year To Check::"))

if len(str(y)) <= 3:
    print("Invalid Input")

else:
    isLeapyear(y)
