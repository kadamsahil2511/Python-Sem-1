# Ques_8
# Write a Python program to check if two given sets have no elements in common.
def no_common_elements(set1, set2):
    return set1.isdisjoint(set2)
set1 = set(map(int, input("Enter elements of the first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of the second set separated by space: ").split()))
print("No common elements:", no_common_elements(set1, set2))