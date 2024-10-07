# Ques 3 Maximum frequency character in String

s3 = input("Enter a string : ")
result = ""
for i in s3:
    if i not in result:
        result += i
print("String after removing duplicates:", result)
