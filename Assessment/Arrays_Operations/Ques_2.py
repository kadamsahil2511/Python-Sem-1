#2. Write a Python program to get the number of occurrences of a specified element in an a1.

import array as ar
a3 = ar.array('i',[])
a = input("Enter All Number Values (Eg: 5 3 7 5) : ").split(" ")
for i in range(0,len(a)):
    a3.append(int(a[i]))
e = int(input("Enter the number of which you would like to find occarance : "))
occ = 0
index = []
for i in range(0,len(a3)):
    if a3[i] == e:
        occ+=1
        index.append(i)
print(f'The Element {e} is occured {occ} times at index(s) {index}')