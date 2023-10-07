

# the use of finally keyword 

try:

       l=[1,2,3,4]

       i=int(input("Enter the index "))

       print(l[i])

except:

       print("Unwanted Error occured:")

finally:

       print("I will always executed:")



# now let us taker a function  example 

def func1():

       try:

              l1=[1,2,3,4]

              b=int(input("Enter your index"))

              print(l1[b])

              return 1

       except:

              print("Unwanted error occured")

              return 0
       finally:

              print("Atlast I got compiled")

x=func1()

print(x)
