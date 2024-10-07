# Ques_Ans
author = 'Sahil Shahaji Kadam'
# Ques 1 Palindrome checker
s1=input("Enter the string : ").lower()
if s1 == s1[::-1]:
    print(s1, "is a palindrome")
else :
    print(s1,'is not a palindrome')

# Ques 2 Lenfunction without using len
s2 = input('Enter the string : ')
l = sum(1 for i in s2)
print("Length of", s2, "is:", l)

# Ques 3 Duplicate eliminator 
s3 = input("Enter a string : ")
result = ""
for i in s3:
    if i not in result:
        result += i
print("String after removing duplicates:", result)

# Ques 4 Character mode
s6 = input("Enter a string: ")
char_freq = {}
for i in s6:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1
max_char = max(char_freq, key=char_freq.get)
print("The character with the maximum frequency is:", max_char)

# Ques 5 character counter
s7 = input("Enter a string: ")
char_count = {}
for i in s7:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)

# Ques 6 Count all the letters, digit and specil symbol from a string
s = input("Enter a string : ")
lc = sum(1 for i in s if i.isalpha())
dc = sum(1 for i in s if i.isdigit())
sc = sum(1 for i in s if not i.isalnum())
print("Letter count:", lc)
print("Digit count:", dc)
print("Special symbol count:", sc)

# Ques 7 Spam folder
emails = []
n_emails = int(input("Enter the number of emails: "))

for i in range(n_emails):
    email = input(f"Enter email {i+1}: ")
    emails.append(email)

v_emails = []
s_emails = []

for email in emails:
    if "@itm.edu" in email:
        v_emails.append(email)
    else:
        s_emails.append(email)

print("\nValid Emails:")
for email in v_emails:
    print(email)

print("\nSpam Emails:")
for email in s_emails:
    print(email)

# Ques 8 Password Validator
password = input("Enter your password : ")
if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char in "!#$%&*+-.?~" for char in password):
    print("Password is valid")
else:
    print("Password is not valid")
