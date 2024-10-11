# Ques_Ans

# Write a Python function to check whether a number falls within a given range.
def num_in_range(num, start, end):
    if not isinstance(num, int) or not isinstance(start, int) or not isinstance(end, int):
        return "Error: Inputs must be integers"
    if start >= num > end:
        return False
    if start <= num <= end:
        return "Yes, the number lies in the range"
    else:
        return "No, the number doesn't lie in the range"
num = int(input("Enter the number you want to check : "))
start = int(input("Enter the starting of range : "))
end = int(input("Enter the ending of range : "))
print(num_in_range(num, start, end))

# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list
def word_length(input_list):
    if not input_list:
        return ("No words found", "No words found")
    shortest = min(input_list, key=len)
    longest = max(input_list, key=len)
    return (shortest, longest)
input_string = input("Enter comma-separated strings: ")
list_of_strings = [s.strip() for s in input_string.split(',')]
result_tuple = word_length(list_of_strings)
print(f"Shortest Word: {result_tuple[0]}")
print(f"Longest Word: {result_tuple[1]}")

# Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list. 
def add_element_into_list():
    my_list = input("Enter elements of the list separated by comma (e.g., 1,2,3): ")
    my_list = [int(x) for x in my_list.split(",")]
    element_to_add = int(input("Enter an element that you want to add into the list: "))
    def add_element():
        my_list  
        return element_to_add not in my_list
    if add_element():
        print(element_to_add, "added into the list successfully.")
        my_list.append(element_to_add)
        print("Updated List: ", my_list)
    else:
        print(element_to_add, "already exists in the list.")

add_element_into_list()

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

# A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])
def perfect_numbers_in_range(lower, upper):
    return [n for n in range(lower, upper + 1) if sum_of_divisors(n) == n]
lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the higher limit : "))
print(perfect_numbers_in_range(lower, upper))

# Write a recursive function that will return the nth term of the Fibonacci sequence.
# The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input('Enter the number you want feb'))
print(fibonacci(n))