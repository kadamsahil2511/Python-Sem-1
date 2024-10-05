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