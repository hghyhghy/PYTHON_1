# updating the elements of one dictionary to another

# creating   teo dictionaries

d1 = {100: 34, 160: 56, 220: 98, 280: 59, 340: 88, 400: 99}

d2 = {300: 45, 350: 54}

# updating the value of d1 with d2

d1.update(d2)

print(d1)

# using clear method to clear a dictionary

d3 = {3: 1, 4: 2, 5: 8}

print(d3)

d3.clear()

print(d3)

# using pop method to rempove a keyvalue pair

d2.pop(300)

print(d2)

# to delete an item from the last we use popitem method

d1.popitem()

print(d1)

# deleting an element using del keyword


del d1[100]

print(d1)
