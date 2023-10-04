
# break statement

for  i in range(10):

       if (i==10):

              break
       
       print("5 X" , i+1 ,"=" , 5*(i+1))



# continue statement 

for k in range(12):

       if(k==10):

              print("Skip the iteration")

              continue
       print("5 X" , i+1 ,"=" , 5*i)


# a while break statement 

i=0

while True:

       print(i)

       i=i+1

       if(i%100==0):

              break

       