# October_11
#Lists
'''
List is created by using '[]' ie. square brackets
l1=list([1,2,3,4,5,6,7,8,9])
#Slicing of list
print(l1[0])
print(l1[0:3])
l2=list("Sahil")
print(l2[0:2])
l1[2]='idk'
print(l1)

# make a loop for appending elements into a list without using any built in function
a=[0,0,0,0,0]    
for i in range(5):
    b=input('Enter an element to make a list : ')
    a[i]=b
print(a)
l4=[1,2,3]
del l4[1:3]
print(l4)
l1=[10,20,30]
l1.append(40)
print(l1)
l1.append([50,60])
print(l1)
print(l1[4].count(50))
l1.extend([70,80])
print(l1)
print(l1.index(40))
l1.insert(5,35)
print(l1)
l1.reverse()
print(l1)
l3=[5,4,3,5,6,7,5,3,2]
l3.sort()
print(l3)
odd_square = [] 
for x in range (1, 11):
    if x%2 ==1 :
        odd_square.append (x**2) 
print(odd_square)


# below list contains square of all # odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x%2 ==1]

print(odd_square)
'''


t1 = (1, 2, 3, 4, 5)

first_element = t1[0]  
last_element = t1[-1]  
sub_tuple = t1[1:4]
length = len(t1)  
new_tuple = t1 + (6, 7) 
repeated_tuple = t1 * 2  
exists = 3 in t1  
count_of_2 = t1.count(2)  
index_of_4 = t1.index(4)  

for element in t1:
    print(element)

list_version = list(t1) 




