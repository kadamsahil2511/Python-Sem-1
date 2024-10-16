# Ques_4
# Write a Python program to remove an empty tuple(s) from a list of tuples.
def remove_empty_tuples(tuples):
    return [tup for tup in tuples if tup]

num_tuples = int(input("Enter the number of tuples: "))
tuples = []

for i in range(num_tuples):
    tuple_str = input(f"Enter tuple {i+1} (comma-separated values): ")
    tup = tuple(map(int, tuple_str.split(',')))
    if tup:
        tuples.append(tup)

result = remove_empty_tuples(tuples)
print("List of non-empty tuples:")
for tup in result:
    print(tup)