# Ques_6 Count all letters, digits, and special symbols from a given string

s = input("Enter a string : ")
lc = sum(1 for i in s if i.isalpha())
dc = sum(1 for i in s if i.isdigit())
sc = sum(1 for i in s if not i.isalnum())
print("Letter count:", lc)
print("Digit count:", dc)
print("Special symbol count:", sc)
