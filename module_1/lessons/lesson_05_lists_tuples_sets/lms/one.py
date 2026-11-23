import random
"""
Task 1. The greatest number

Write a Python program to get the largest number from a list of 10 random numbers.

Use only a while loop and the random module to generate numbers.
Find the largest number with a while loop, without max().
Print the list first. At the end, print max(numbers) to check your result.
Add a comment # Trace: and, for your printed list, write the value of your “largest so far” variable after each of the first three steps.
"""
print(f"{'Task 1. The greatest number':*^80}")
numbers = list(random.randint(0, 100) for _ in range(10))
i = 0
max_value = 0
while i < len(numbers):
    if numbers[i] > max_value:
        max_value = numbers[i]
    if i % 3 == 0:
        print(f"# Trace curent max value: {max_value}")
    i += 1


print(f"The random list {numbers = }")
print(f"{max(numbers) = }")
print(f"The max value find in while loop is {max_value = }")



"""
Task 2. Extracting numbers

Make a list that contains all integers from 1 to 100. Find all integers that are divisible by 7 but are not multiples of 5, store them in a separate list and print the result.

Use only a while loop for iteration.
Before running the program, write as a comment the first three numbers you expect and explain why 35 is not in the list.
"""
print(f"{'Task 2. Extracting numbers':*^80}")
numbers_sequence = list(range(0, 100))
needed_list = list()

i = 0
while i < len(numbers_sequence):
    if numbers_sequence[i] % 7 == 0 and numbers_sequence[i] % 5 != 0:
        needed_list.append(numbers_sequence[i])

    i += 1

print(f"Numbers from 1 to 100 divisible by 7 and not multiples 5 is {needed_list}")

"""
Task 3. Common numbers without duplicates

Generate two lists, first_list and second_list, each containing 10 random integers from 1 to 10. Make a third list containing the integers that appear in both lists, without duplicates, and print it.

Use only a while loop and the random module to generate numbers.
Run the program once and copy both generated lists into a comment. Under them, write by hand which numbers must be in the result. Compare this with what your program printed.
"""
print(f"{'Task 3. Common numbers without duplicates':*^80}")
first_list = list(random.randint(1, 10) for _ in range(10))
second_list = list(random.randint(1, 10) for _ in range(10))

i = 0
j = 0
intersection_array = list()
while i < len(first_list) and j < len(second_list):
    if first_list[i] == second_list[j] and first_list[i] not in intersection_array:
        intersection_array.append(first_list[i])

    i += 1
    if i == len(first_list):
        j += 1
        i = 0

print(f"First list: {first_list = }")
print(f"Second list: {second_list = }")
print(f"Intersection list: {intersection_array = }")

"""
Task 4. Find the bugs

This program should generate 10 random numbers and print the unique ones, but it crashes. It has two bugs.

import random

numbers = []
i = 0
while i < 10:
    numbers = numbers.append(random.randint(1, 5))
    i += 1

unique_numbers = {}
i = 0
while i < len(numbers):
    unique_numbers.add(numbers[i])
    i += 1

print("All numbers:", numbers)
print("Unique numbers:", unique_numbers)
Run the program and copy the last line of the error message into a comment.
Fix this bug and run the program again. When it crashes with a new error, copy that error too and fix it.
Above each fix, add a comment # Bug: explaining in your own words what was wrong.
"""
print(f"{'Task 4. Find the bugs':*^80}")

numbers = list()

i = 0
while i < 10:
    numbers.append(random.randint(1, 5))
    """
    Traceback (most recent call last):
      File "lms/one.py", line 108, in <module>
        numbers = numbers.append(random.randint(1, 5))
    AttributeError: 'NoneType' object has no attribute 'append'
    
    we replace numbers with return value of numbers.append(random.randint(1, 5)) and this value = None,
    None doesn't have 'append'
    """
    i += 1

unique_numbers = set()
i = 0
while i < len(numbers):
    unique_numbers.add(numbers[i])
    """
    Traceback (most recent call last):
      File "lms/one.py", line 124, in <module>
        unique_numbers.add(numbers[i])
    AttributeError: 'dict' object has no attribute 'add'
    
    we create dict, but there need create Set, empty Set creates only with set()
    """
    i += 1

print(f"The numbers list {numbers = }")
print(f"Unique numbers in the numbers list {unique_numbers = }")