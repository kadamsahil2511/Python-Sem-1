# Ques_6
# Write a Python a function to find the union and intersection of two lists.
def union_and_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection
list1 = input("Enter the list 1 elements separated by space : ")
list2 = input("Enter the list 2 elements separated by space : ")
print(union_and_intersection(list1, list2))
