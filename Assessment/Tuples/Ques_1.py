# Ques_1

# Write a Python program to compute the element-wise sum of given tuples. 
# Original :    (1, 2, 3, 4)   (3, 5, 2, 1)   (2, 2, 3, 1)
# Element-wise sum of the said tuples:  (6, 9, 8, 6)
def element_wise_sum(tuples):
    result = []
    for tup in tuples:
        result_tuple = [sum(pair) for pair in zip(tup)]
        result.append(result_tuple)
    return result

num_tuples = int(input("Enter the number of tuples: "))
tuples = []

for i in range(num_tuples):
    tuple_str = input(f"Enter tuple {i+1} (comma-separated values): ")
    tup = tuple(map(int, tuple_str.split(',')))
    tuples.append(tup)

result = element_wise_sum(tuples)
print("Element-wise sum:")
for i in range(len(result[0])):
    print(f"Sum at position {i+1}: {sum([t[i] for t in result])}")

