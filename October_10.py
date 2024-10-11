# October_10
'''
Scope of variables
1. Gloabal Variables
2. Local Variables
#eg
g1=10
def sample(n):
    l1=0
    global g2
    g2=20
    l1=l1+n+g1+g2
    print(l1)
sample(10)
print("Global variable", g1)
print("GLobal variable within function", g2)
# print("Local Variable", l1)

#eg2
a=20
def scope():
    a=10
    print('a=',globals()['a'])
    print('a=',a)
scope()
'''
#Recursion
'''
It is the processs where function call itself from it's own body and that function is called as recusive function
'''
#Factorial of number of recursion
def factorial(n):
    if n==1:
        return 1
    else :
        return n*factorial(n-1)

print("The factoial is",factorial(1))