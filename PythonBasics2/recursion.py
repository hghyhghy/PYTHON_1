# recursive method in python

# finding a factorial of a number in python using recursion

# creating a function named  factorial


def factorial(n):
    
    if n == 1 or n == 0:
        
        return 1
    else:
        
        return n * factorial(n - 1)


print(factorial(3))

print(factorial(4))

print(factorial(5))


# printing the fibonacci series in python using recursion


def fibonacci(n):
    
    if n == 0:
        
        return 0

    elif n == 1:
        
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# if __name__ == "__main":
n = 9

for i in range(n + 1):
    
    print("The fibonacci series is ", fibonacci(i))
