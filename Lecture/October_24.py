# October_24
'''import os, time
os.mkdir("Temp Folder")
print(os.getcwd())
os.chdir("Temp Folder")
print(os.getcwd())
os.chdir("/Users/sahilshahajikadam/Documents/Python-Files/Lecture")
print(os.getcwd())
time.sleep(5)
os.rmdir("Temp Folder")
'''
#File positions
'''
1.Tell
2.seek(offset,[,form])
offset has 3 values 0(start), 1(curent), 2(end)
#File operations using CSV
# pos=f.tell() 
# print(pos)
# f=open("t1.txt","rb")
# f.seek(-15,2) 
# print(f.readline())

# csvfile=open("../Dependencies/iris.csv", "r") 
# first_line= csvfile.readline() 
# print(first_line)

# with open("../Dependencies/iris.csv", "r") as csvfile: 
#     first_line= csvfile.readline() 
#     print(first_line)

# with open("../Dependencies/iris.csv", "r") as csvfile: 
#     all_lines = csvfile.readlines() 
#     print(all_lines)

with open("../Dependencies/iris.csv", "a") as csvfile:
    tba = "6.0,3.1,5.0,2,Iris-virginica"
    csvfile.write(tba)
'''

# Exception handeling in Python
'''
try:
    print(x) # type: ignore

except Exception as e:
    print("An exception occurred", e) 
print("End of program")
try:
    print(x)

except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
try:
    a=[1,2,3,4]
    print(a[4])
except IndexError:
    print("Out of an index") 
print("End of program")

try:
    print("Hello")
except:
    print("Something went wrong")
else: 
    print("Nothing went wrong")
try:
    age=int(input("Enter the age ? "))
    if age<18:
        raise ValueError;
    else:
        print("the age is valid")
except ValueError: 
    print("The age is not valid")

try:
    print("hello",i) # type: ignore
except NameError:
    print("Name error , i not defined")
# except Exception as e:
#     print("Error!",e)
# # print("End of program")

finally: # not related to try or except , it will run after program completes
    print("End of program")
'''
class MyError(Exception):
    def __init__(self,msg):
        self.messaging=msg
    def displayError(self):
        return self.message
try: 
    a=int(input("Enter a : ")) 
    b=int(input("Enter b : "))
    if b==0:
        raise MyError("value of b cannot be 0")
    c=a/b;

except MyError as e:
    print("Error: ",e.displayError())
except: 
    print("Error occured")
else:
    print("division is : ",c)
finally:
    print("In finally")