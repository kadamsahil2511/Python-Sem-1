# October_21
'''
File I/O
Syntax
file_object=open("file path", "mode")
file_object.close()
'''
#For writing data in a new file
# f=open("/Users/sahilshahajikadam/documents/python-files/myfile.txt",'w') # used physical path
f=open("./myfile.txt",'w') #used relative path
data="Data"
f.write(data)
# f.close()
#For reading a data from an existing file
f=open("./myfile.txt",'a') #used relative path
data="\nHello"
f.write(data)
f=open("./myfile.txt",'r') #used relative path
data=f.readlines()
print("Data : ",data)
print("File Contentes : ", data)
c=1
for line in data:
    print(c,line)
    c+=1
f.close()
