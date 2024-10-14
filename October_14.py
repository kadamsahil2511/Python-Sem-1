# October_14
'''
Sets, A collection which is unordered and unindexed in python sets are written with curly brackets
s= {1,2,3,4,5}
t={6,7,8,9}
s=set()
s.add(10)
# s.clear()
# s.copy()
print(s.difference(t))
print(s.intersection(t))
print(s.isdisjoint(t))
print(s.issubset(t))
print(s.issuperset(t))
# s.pop()
# s.remove()
# s.symmetric_difference()
union=s.union(t)
# s.update()
print(union)
'''

# Create a menu to add a member in a goup and to remove a member in the group use set to make the app using set
group={}
group=set()
def main():
    a=(int(input('''Welcome to the admin panel, enter which operation number you want to perform
          1.View all the members
          2.Add a member
          3.Remove a member\n''')))
    if a==1:
        n=0
        for i in range(len(group)):
            print(i,end='\n')
    elif a==2:
        n=int(input("How many members you want to add : "))
        for i in range(n+1):
            b=input("Enter the member you want to add : ")
            group.add(b)
    elif a==3:
        b=input("Enter the member you want to remove : ")
        group.remove(b)
    else :
        print("enter a valid input")
main()