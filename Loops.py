# importing time module


import time

a = int(input("Enter Your age :"))

print("Your age is ", a)

# if else statement

if a > 18:
    print("You can drive and vote ")

else:
    print("You can not drive ")

applePrice = 210

myBudget = 190

if applePrice <= myBudget:
    print("Add 1kg apple to the cart ")

else:
    print("Don not add apple to the cart ")


applePrice = 210

budget = int(input("Enter Your Budget"))

if applePrice <= budget:
    print("Add 1kg apple to the cart ")

else:
    print("Don not add apple to the cart ")


s = int(input("Enter A Number "))

if s < 0:
    print("The number is negative")

elif s == 0:
    print("The number is zero")

else:
    print("The number is positive")


# #nested loops in python

n1 = int(input("Your number \n"))

if n1 < 0:
    print("The number is negative")

elif n1 > 0:
    if n1 <= 10:
        print("The number lis between 0 and 10")

    elif n1 >= 10 and n1 <= 20:
        print("The number is between 10 and 20")

    else:
        print("The number is beyond 20")
else:
    print("The entered number is zero")


timestamp = time.strftime("%H:%S:%M")

print(timestamp)

timestamp = time.strftime("%H")

print(timestamp)

timestamp = time.strftime("%S")

print(timestamp)

timestamp = time.strftime("%M")

print(timestamp)
