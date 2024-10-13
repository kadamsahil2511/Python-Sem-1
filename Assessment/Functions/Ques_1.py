# Ques_1
# Write a Python function to check whether a number falls within a given range.
def num_in_range(num, start, end):
    if not isinstance(num, int) or not isinstance(start, int) or not isinstance(end, int):
        return "Error: Inputs must be integers"
    if start >= num > end:
        return False
    if start <= num <= end:
        return "Yes, the number lies in the range"
    else:
        return "No, the number doesn't lie in the range"
num = int(input("Enter the number you want to check : "))
start = int(input("Enter the starting of range : "))
end = int(input("Enter the ending of range : "))
print(num_in_range(num, start, end))