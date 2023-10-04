def calculate_gmean(a, b):
    mean = (a * b) / (a + b)

    print(mean)


# creating another fucntion


def isGreater(x, y):
    if x > y:
        print("X is greater than y")

    elif x < y:
        print("Y is greater than x")

    else:
        print("The numbers are equal ")


# creating another function


def isLesser(a, b):
    pass


# that  PASS  means to simply pass the function

a = 2

b = 3

# calling the function

calculate_gmean(a, b)

# calling the function

isGreater(a, b)

# let us take another value

c = 23

d = 32

# calling the function

calculate_gmean(c, d)

# calling the function

isGreater(c, d)

# creating another function


def AverageOf(a, b):
    average = (a + b) / 2

    print(average)


AverageOf(5, 5)


# creating default arguments


def isDefault(a=5, b=5):
    Default = (a + b) / 2

    print(Default)


isDefault()


# creating a  function of name


def name(fname, mname="Subham", lname="Sarkar"):
    print("Hello", fname, mname, lname)


name("Mr")

# functions with 3 arguments


def threeAverage(a, b, c=1):
    average = (a + b + c) / 3

    print(average)


threeAverage(3, 4)


def avg(*numbers):
    sum = 0

    for i in numbers:
        sum = sum + i

        print("Average of the numbers are ", (sum) / len(numbers))


avg(1, 2, 3)


def avg(*numbers):
    sum = 0

    for i in numbers:
        sum = sum + i

        return (sum) / len(numbers)


c = avg(2, 3, 4, 5)

print(c)
