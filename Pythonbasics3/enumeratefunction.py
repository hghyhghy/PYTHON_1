# to understand an enumerate program first we need  to take an example

marks = [12, 34, 56, 99, 78, 89, 23]

index = 0

for mark in marks:
    print(mark)

    if index == 3:
        print("Subham !! You have done awesome")

        index += 1

# the following code is an enumerate function

for index, mark in enumerate(marks)
:
    print(mark)

    if index == 3:
        
        print("Subham !! You have done awesome")

        index += 1

# starting from a specific value

for index, mark in enumerate(marks, start=1):
    
    print(mark)

    if index == 3:
        
        print("Subham !! You have done awesome")


# taking an exmaple  of a single string 

s="Subham"

for index , c in enumerate(s):
    
    print(c)

    if(index==3):
        
        print("I love Myself")