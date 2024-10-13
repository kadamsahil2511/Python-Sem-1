#4. Write a  Python program to find the missing number in a given array of 5 continuous numbers.

import array as ar
a4 = ar.array('i', [])
a = input("Enter All Number Values (Eg: 1 2 . . .) : ").split(" ")

for i in range(0, len(a)):
    a4.append(int(a[i]))
m_num = None

for i in range(1, len(a4)):
    if a4[i] != a4[i - 1] + 1:
        m_num = a4[i - 1] + 1
        break

if m_num is None:
    print("The numbers are in continuous order.")
else:
    print("The numbers are NOT in continuous order.")
    print(f"Missing Number: {m_num}")