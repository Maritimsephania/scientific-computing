#Date types declaration
integer1 = 1 # creates a variable of type of int
float1 = 34.02 # creates a variable of type of float
complex1 = 2 + 5j # creates a variable of type complex
list1 = [1, "Volvo", 3.14, True] # creates a variable of type of list
tuple1 = (1,"Volvo",3.14, True)# creates a variable of type tuple
mixed_dict = {1: "apple", "color": "red", "price": 1.99} #Creates a variable of type dict
number_set = {1,2,3,4,5} #creates a set of numbers
is_active = True #creates a bool variable

#Printing variables types for each of the variables.
print(type(integer1))
print(type(float1))
print(type(complex1))
print(type(list1))
print(type(tuple1))
print(type(mixed_dict))
print(type(number_set))
print(type(is_active))

# Type conversion examples
float2 = float(integer1)  # Converting integer to float
num2 = int(float1)   # Converting float to integer

# Printing converted values
print(f"num2: \t{num2}")
print(f"float2: {float2}")