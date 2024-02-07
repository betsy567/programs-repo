li=[1,22,67,24,88,33]
print("The list :",li)
# Use list comprehension to create a new list without even numbers
li = [num for num in li if num % 2 != 0]
print("After removal:", li)

