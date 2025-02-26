# Getting integer entered by user.
integer_by_user = int(input("Enter any value:"))

#Fuction to check if a number is odd or even
def is_even(number):
    return number%2==0

# Test the function
result = is_even(integer_by_user)
print(result)  # Output: True
# To create a list of even numbers for 0 to 50
count =0
even_numbers =[]

for count in range(51):
    if is_even(count):
        even_numbers.append(count)
print(even_numbers)

# Printing 0 to 10 using while loop

counter1 = 0
counter2 = 10
while counter1 <= 10:
  print("Counter is : ",counter2-counter1)
  counter1 += 1


