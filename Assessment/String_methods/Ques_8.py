# Ques_8 You are tasked to create a simple password validator. The validation rules are as follows:
# Password length of at least 8 characters.
# At least one uppercase character.
# At least one lowercase character.
# At least one "special" character from the following set of characters: "!#$%&*+-.?~".

password = input("Enter your password : ")
if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char in "!#$%&*+-.?~" for char in password):
    print("Password is valid")
else:
    print("Password is not valid")
