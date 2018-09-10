"""
while loops
"""
""" take-away point: don't use a function's name as a variable """
"""
i = 0
numbers = []

while i < 6:
     print(f"At the top i is {i}")
     numbers.append(i)

     i = i + 1
     print("Numbers now: ", numbers)
     print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
"""
# use for loop

i = 0
numbers = []

for i in range(0,6):
     print(f"At the top i is {i}")
     numbers.append(i)
     print("Numbers now: ", numbers)
     print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)


'''
# make a user defined function

def while_function(input_number,increase_by):
    i = 0
    numbers = []

    while i < input_number:
         print(f"At the top i is {i}")
         numbers.append(i)

         i = i + increase_by
         print("Numbers now: ", numbers)
         print(f"At the bottom i is {i}")
# ask user to input a number
what_in = input("input a number: ")
# convert string to int
what_in = int(what_in)
# ask user increase by how much per loop
gap = input("increase? ")
gap = int(gap)

# run your function
while_function(what_in,gap)
'''
