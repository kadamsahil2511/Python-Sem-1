# Sets and its operations

# Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    return list(set(input_list))
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(remove_duplicates(input_list))

# Write a Python function that takes two lists and returns True if they have at least one common member.
def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))
list1 = input("Enter the list 1 elements separated by space : ")
list2 = input("Enter the list 2 elements separated by space : ")
print(have_common_member(list1, list2))

# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even_numbers(input_list):
    return [num for num in input_list if int(num) % 2 != 0]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(remove_even_numbers(input_list))

# Write a Python program to find the second smallest number in a list.
def second_smallest(input_list):
    unique_list = list(set(input_list))
    unique_list.sort()
    return unique_list[1] if len(unique_list) > 1 else None
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(second_smallest(input_list))

# Write a Python program to split a list every Nth element.
def split_list(input_list, n):
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
n = int(input("Enter the Nth element : "))
print(split_list(input_list, n))

# Write a Python a function to find the union and intersection of two lists.
def union_and_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection
list1 = input("Enter the list 1 elements separated by space : ")
list2 = input("Enter the list 2 elements separated by space : ")
print(union_and_intersection(list1, list2))

# Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
def is_palindrome(input_list):
    return input_list == input_list[::-1]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(is_palindrome(input_list))
