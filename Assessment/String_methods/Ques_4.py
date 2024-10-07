# Ques_4 Maximum frequency character in String

s6 = input("Enter a string: ")
char_freq = {}
for i in s6:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1
max_char = max(char_freq, key=char_freq.get)
print("The character with the maximum frequency is:", max_char)
