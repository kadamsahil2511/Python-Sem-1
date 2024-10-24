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
'''
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