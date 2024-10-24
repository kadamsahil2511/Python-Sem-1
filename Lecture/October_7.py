#Oct_7
#Built-in functions in string
s1="Python programming"
'''
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())

print(s1.isupper())
print(s1.islower())
print(s1.istitle())
print(s1.center(31,'#'))
print(s1.count('o',5))
print(s1.startswith('Py'))
print(s1.endswith('on'))
print(s1.find("o",5))
# if data is not found it returns '-1' ~ none 
print(s1.index("o"))
# print(s1.replace('Python', 'JavaScript'))
# print(v1.identifier())
print(s1.isnumeric())
print(s1.isprintable())
print(s1.isspace())
v1=['Number1','Number2','Number3']
print(' '.join(v1))
a= ' '.join(v1)
print(a.split())
print(a.split(' ', maxsplit=1))
msg="Yo !\n me hu Schinchan Nohara"
print(msg.splitlines()) 

print('     yo!     '.strip())
s3=print('!!!Hey!!!!'.strip('!'))

# Arrays in Python
# arays are homogenous where as other data types are heterogenous
arr= a.array('d', [9.1,9.2,9.3])
print(arr)
print('First element :', arr[0])
print('second last element :', arr[-2])
print('last element :', arr[-1])

'''
import array as a
# Converting list/tuple into an array
num=[1,2,3,4,5,6,7,8,9,0]
num_a= a.array('i',num)
print(num_a)

# Search and element in an array
no=int(input('Enter the digit between 0 and 9'))
if no in num_a:
    print('Yes', no, 'is in the array')