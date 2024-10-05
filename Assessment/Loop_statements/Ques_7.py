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
