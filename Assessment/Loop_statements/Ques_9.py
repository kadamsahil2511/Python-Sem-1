#9. Pattern Printing

print("(a) Number Pattern")
for i in range(5, 0, -1): 
    for j in range(i, 0, -1):
        print(j, end=" ")
    print() 
print("-"*20)
print("(b) Star Pattern")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")