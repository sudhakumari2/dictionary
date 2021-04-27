f=open("people.txt","a")
f.write("sarika\n sudha\n ruchi\n somi")
f=open("people.txt","r")
people=[]
c=0
for name in f:
    c+=1
    people.append(name)
print(c)
print(people)

# def file_size(fname):
#         import os
#         statinfo = os.stat(fname)
#         return statinfo.st_size

# print("File size in bytes of a plain file: ",file_size("test.txt"))

# # check file is closed or not
# f = open('people.txt','r')
# print(f.closed)
# f.close()
# print(f.closed)