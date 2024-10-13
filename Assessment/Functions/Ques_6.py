# Write a recursive function that will return the nth term of the Fibonacci sequence.
# The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input('Enter the number you want feb'))
print(fibonacci(n))