# Ques_5 Write a Python program to count the number of characters in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

s7 = input("Enter a string: ")
char_count = {}
for i in s7:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)
