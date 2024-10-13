# Ques_4
# Write a program to implement these formulae of permutations and combinations. 
# Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
# Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!
# A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def permutations(n, r):
    return factorial(n) / factorial(n - r)
def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
n = int(input("Enter n value : "))
r = int(input("Enter r value : "))
print("Permutations:", permutations(n, r))
print("Combinations:", combinations(n, r))