#Loops statments assignments
author = "Sahil Shahaji Kadam"

#1. Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

#2. Counting Digits in a Number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10  
    count += 1

print("Number of digits:", count)

#3. Reversing a List
list1 = [1,2,3,4,5,6,7,8,9,0]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i], end=",") 

#4. Prime Numbers within a Range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end = ",")

#5. Fibonacci Series
terms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence up to", terms, "terms:")
while count < terms:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

#6. Reversing an Integer
num = int(input("Enter an integer: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: ", reversed_num)

#7. Sum of Evens and Odds
even_sum = 0
odd_sum = 0

for i in range(0, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of all evens is", even_sum) 
print("And the sum of all odds is", odd_sum)

#8. Counting Letters and Digits
string = input("Sample Data : ")
letters = 0
digits = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters", letters, "  Digits", digits) 

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