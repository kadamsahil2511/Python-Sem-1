# Ques_9
# Write a Python program toGet Only unique items from two sets
def unique_items(set1, set2):
    return set1.symmetric_difference(set2)
set1 = set(map(int, input("Enter elements of the first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of the second set separated by space: ").split()))
print("Unique items from both sets:", unique_items(set1, set2))