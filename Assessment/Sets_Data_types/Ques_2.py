# Ques_2
# Write a Python function that takes two lists and returns True if they have at least one common member.
def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))
list1 = input("Enter the list 1 elements separated by space : ")
list2 = input("Enter the list 2 elements separated by space : ")
print(have_common_member(list1, list2))