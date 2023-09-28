# setting a name string

names = "Subham,Shreyashi"

#  getting a specific name by giving starting index and ending index

print(names[0:6])

# getting the length of the name by len()  function

print("The length of the string  is ")

print(len(names))


# let us  take another example


string = "Mango"

len1 = len(string)

print("The length of the mango is ", len1)

# negative slicing

string1 = "Django"

print(string1[-3:-1])

# changing the string to upper case in python

string_1 = "shreyashi"

print("The uppercase of the ", string_1, "is")

print(string_1.upper())

# changing the string to lower  case in python

print("The uppercase of the ", string_1, "is")

print(string_1.lower())

string_2 = "subham !!!!"

# stripping the trailing characters

print(string_2.rstrip("!"))

# changing the occurances of  string by replace()  function


string3 = "Subham"

# changing the name with shreyashi

print(string3.replace("Subham", "shreyashi"))

# splitting the string with split()  function

name1 = "su bh am"

print(name1.split(" "))

# capitalizing the first letter of a string

name3 = "introduction to python"

print(name3.capitalize())

# aligning  the string to center by center()  function


stc = "Welcome to python  "

print(stc.center(50))

print(len(stc))

print(len(stc.center(50)))

# counting the number of occurance in a string by count()  function

stc1 = "subham and shreyashi loves each other "

print(stc1.count("s"))

# checking wheather a string is ends with some particular letter or not


nam = "subham and shreyashi loves each other"

print(nam.endswith("r"))

print(nam.endswith("other"))

# finding the first occurance with find() method

num1 = "Subham is an engineer , he is a good boy "

print(num1.find("is"))

print(num1.count("is"))

# checking wheather a string contains  alphanumeric characters or not by using isalnum()  method

na = "Subham090200a"

print("Is our string contains alphanumeric contents ? ")

print(na.isalnum())

# checking for alpha characters not numeric bu isalpha()  method

na1 = "subham00"

print(na1.isalpha())

# checking if lower case is present or not

n = "SuBham"

print(n.islower())

print(n.isprintable())

n1 = "SuBham\n"

print(n1.isprintable())

# checking whaether a string contains white space or not

n2 = "subham   is    a    good   boy "

print(n2.isspace())

n3 = "         "

print(n3.isspace())

# istitle()  return true only the first letter is capital


nun = "Cimonoseki"

print(nun.istitle())

# it makes upper case lower and vice versa


print(nun.swapcase())




