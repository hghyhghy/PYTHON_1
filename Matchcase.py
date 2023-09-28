

x=int(input("Enter your Number:"))

match x:

       case 0:

              print("The number is zero:")

       case 5:

              print("The number is " , 5)


       case _ if(x!=90):

              print("X is not 90")


       case _ if(x!=80):

              print("X is not 80")
       

       case _:

              print(x)       

       
              

