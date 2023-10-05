# creating dictionaries in python

dic = {"Name": "Subham Sarkar", "Age": 20, "Gender": "Male"}

print(type(dic))

print(dic["Name"])

# creating dictionaries with integer values

dic1 = {100: "Subham", 200: "Shrayoshi", 300: "Taskin Hussain"}

# accessing the values

print(dic1[100])

# accessing the value by info.get()  methods

print(dic.get("Gender"))


# accessing all the keys at a same time by methods

print(dic1.keys())

print(dic.keys())

# accessing elements by using for loops

for key in dic.keys():
    print(dic[key])


# accessing all the valus by .valus() methods

print(dic1.values())

# accessing the elements in key value pair by using .item() methods 

print(dic.items())



