# exception handling in python

a = int(input("Enter your Number:"))

print(f"Multiplication table of {a}  is :")

# running a for loop

for i in range(1, 11):
    print(f"{int(a)} X {i}={int(a)*i}")


# the upper one is a normal program

# but if we have doubt that we mat get error we can write like this

b = input("Enter your Number:")


print(f"Multiplication table of {b}  is :")


try:
    for k in range(1, 11):
        print(f"{int(b)} X {k}={int(b)*k}")

except:
    print("Invalid Input")


print("Compilation error!!")

# eliminating the value error 

try:
    
    s=int(input("Enter a number "))

except:
    
    print("Number entered is not an integer")
