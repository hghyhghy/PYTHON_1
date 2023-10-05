# joining two methods in set bu union methods

# creating a new set

s1 = {1, 2, 3, 4, 3}

s2 = {5, 6, 7}

# printing the union of two sets

print(s1.union(s2))

# updating the set by update method

s1.update(s2)

print(s1)

# intersection methods in set

# this method  is used to get the common element in two sets

animal = {"Tiger", "Lion", "Cheetah"}

animal1 = {"Ostrich", "Rats", "Cheetah", "Lion"}

# using the intersection method

print(animal.intersection(animal1))

# use of symmetric difference method to get the elements which is not common

list1 = {"Kolkata", "Dhaka", "Islamabad", "colombo"}

list2 = {"Amsterdam", "Dhaka", "Kolkata", "Berlin", "london"}

temp = list1.symmetric_difference(list2)

print(temp)

temp1 = list1.difference(list2)

print(temp1)

# use of disjoint method

# to check for any common element return boolean

temp3 = list1.isdisjoint(list2)

print(temp3)

# use of superset method

# toc check wheather element is present in one set or  not


temp4 = list1.issuperset(list2)

print(temp4)

# the subset method in python

temp5 = list2.issubset(list1)

print(temp5)

# add() method to add new element in the set

list1.add("Vrindavan")

list1.add("Mathuar")


print(list1)

# remove() method to delete an element from the set

list1.remove("Islamabad")

print(list1)

list2.discard("Berlin")

print(list2)

# del keyword is used to delete the entire set

l1 = {1, 2, 3, 4, 5}

del l1

# checking wheather an element is present in the list or not by if else loop 

l2={"Apple" ,"Pineapple" ,"Mango" ,"Orange"}

if "Mango" in l2:

       print("Yes mango is present ")

else:
       print("No we couldnot find mango")
