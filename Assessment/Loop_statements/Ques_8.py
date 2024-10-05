#8. Counting Letters and Digits
string = input("Sample Data : ")
letters = 0
digits = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters", letters, "  Digits", digits) 
