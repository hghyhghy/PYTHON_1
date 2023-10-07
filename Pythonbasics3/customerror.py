

# raising custom error using a simple program 

a=int(input("Enter any value between 5 and 9:"))

if (a<5 or a>9):

       raise ValueError("Value does not lies between 5 or 9")
