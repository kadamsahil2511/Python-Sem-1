# Ques_6
# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
import functools

def tuple_product(tup):
    return functools.reduce(lambda x, y: x * y, tup)

num_tuples = int(input("Enter the number of tuples: "))
tuples = []

for i in range(num_tuples):
    tuple_str = input(f"Enter tuple {i+1} (comma-separated values): ")
    tup = tuple(map(int, tuple_str.split(',')))
    tuples.append(tup)

result = []
for tup in tuples:
    result.append(tuple_product(tup))
print("Products:")
for i in range(len(result)):
    print(f"Product of tuple {i+1}: {result[i]}")