name = "Subham"

Friend = "Swarnodip"

AnotherFriend = "Tonmoy"

print("The friends of ", name, "is", Friend, AnotherFriend)

# multi lines string

string1 = """Hey Subham , I am Here To meet You , How Are You Buddy"""

print(string1)

# printing the index value of a string

print("The first letter of ", name, "is ")

print(name[0])

print(name[0] + name[1])

print(name[0] + name[1] + name[2])

print(name[0] + name[1] + name[2] + name[3])

print(name[0] + name[1] + name[2] + name[3] + name[4])

print(name[0] + name[1] + name[2] + name[3] + name[4] + name[5])

print("Lets use a for loop")

for character in name:
    print(character)


print("Let use for loop for big string ")

for character in string1:
    print(character)
