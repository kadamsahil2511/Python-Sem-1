#Q1. Write a Python program to reverse the order of the items in the array.

import array as ar
a1 = ar.array('i',[2, 4, 6, 3, 8, 7, 9, 1])
r_a=ar.array('i',[])
for i in range(1,len(a1)+1):
    r_a.append(a1[-i])
print(r_a)