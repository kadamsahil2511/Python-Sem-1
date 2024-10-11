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
#Factorial of number of recursion
def factorial(n):
    if n==1:
        return 1
    else :
        return n*factorial(n-1)

print("The factoial is",factorial(1))
'''

# Python Modules
'''

import mymodule
mymodule.sayhello("Sahil")
mymodule.greet("Morning")
from mymodule import bye
bye("Sahil")
'''
import math
print(dir(math))
print("math.pi", math.degrees(0.5235987755982988))
print("math sin", math.sin(0.5235987755982988))
print("math cos", math.cos(0.5235987755982988))
print("math tan", math.tan(0.5235987755982988))
print("math log", math.log(10))
print("math log 10", math.log10(10))
print("math power", math.pow(2,4))
print('math ceil',math.ceil(4.556))
print("math floor", math.floor(4.556))

import random
print(random.random())
print(random.randint(1,200))
print(math.floor(random.random()))

print(random.randrange(1,10,2))
print(random.choice('Computer'))

num=[1,2,3,4,5,6,7,8,9]
random.shuffle(num)
print(num)