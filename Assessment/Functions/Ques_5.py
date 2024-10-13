# Ques_5
# A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])
def perfect_numbers_in_range(lower, upper):
    return [n for n in range(lower, upper + 1) if sum_of_divisors(n) == n]
lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the higher limit : "))
print(perfect_numbers_in_range(lower, upper))