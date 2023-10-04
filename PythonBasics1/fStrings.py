# formatting the f string

info = "Hello myname is {}  and I am from {}"

name = "Subham"

country = "India"

print(info.format(name, country))


# now the function of f  string


name = "Subham Sarkar"

school = "Jodhpur park Boys School"

print(f"Hello My name is {name}  and My school was {school}")

fruit = "apple"

price = 49.9999

print(f"You get {fruit}  for only {price:.2f} dollars")

# the (.2f) will take  decimal value upto 2 digits


# calculation inside the f string


print(f"{2*30}")


print(f"Hello My name is {{Subham}} and i am from {{Kolkata}} ")
