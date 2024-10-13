# 3. Write a Python program to find out if a given array of integers contains any duplicate elements.

import array as ar
a2 = ar.array('i', [])
a = input("Enter All Number Values (Eg: 1 2 3 4 5) : ").split(" ")
for i in range(0, len(a)):
    a2.append(int(a[i]))

duplicates = False
checked = set()

for num in a2:
    if num in checked:
        print("Yes the array contains duplicates!")
        duplicates = True
        break
    checked.add(num)

if not duplicates:
    print("No the array does not contain duplicates.")