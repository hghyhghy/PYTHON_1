# printing the name of the folders by using os in python

import os

folders = os.listdir("Data")

print(folders)

# printing the folders in a list

for folder in folders:
    print(folder)

# checking for any content inside a folder using os in python

for folder in folders:
    print(folder)
    print(os.listdir(f"Data/{folder}"))


# if we want to print the current directory by using os module we can use the following method


print(os.getcwd())

# if we want to change directory we can use the chdir () method

# like print (os.chdir())
