#5. Replace all odd numbers in the given array with -1

import array as ar
a5 = ar.array('i', [])
a = input("Enter All Number Values (Eg: 1 4 . . .) : ").strip().split(" ")

for i in range(0, len(a)):
    a5.append(int(a[i]))
for i in range(0,len(a5)):
    if a5[i] % 2 != 0:
        a5[i]=-1
print(a5)