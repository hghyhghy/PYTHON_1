import math

# if we want to import only two functions in that case we use from keyword

from math import sqrt, pi

# use of "as"  keyword >> nwe can write like that 

# import math module  as m or

# from math import pi , sqrt as s

# math.floor(4.2323)

# getting the square root from math

s = 9

result = math.sqrt(s)

print(result)

# now by using a function 


def ofSquareroot(s):
    result = sqrt(s) * pi

    print(result)


temp = ofSquareroot(100)

print(temp)

# by using dir ()  function we can print all the functions present in math 

print(dir(math))
