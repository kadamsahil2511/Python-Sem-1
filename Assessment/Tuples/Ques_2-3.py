# Ques_2-3

# Write a Python program to convert a given list of tuples to a list of lists. 
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
def tuple_to_list(tuples):
    result = []
    for tup in tuples:
        result.append(list(tup))
    return result

num_tuples = int(input("Enter the number of tuples: "))
tuples = []

for i in range(num_tuples):
    tuple_str = input(f"Enter tuple {i+1} (comma-separated values): ")
    tup = tuple(map(int, tuple_str.split(',')))
    tuples.append(tup)

result = tuple_to_list(tuples)
print("List of lists:")
for sublist in result:
    print(sublist)

# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
print(tuple_to_list([(1, 2), (2, 3), (3, 4)])) 