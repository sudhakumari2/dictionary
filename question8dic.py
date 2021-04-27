# question number 8
students=[]
marks=[]
i=1
while i<=10:
    student=input("enter sudent name")
    students.append(student)
    j=1
    while j<=1:
        num=int(input("enter marks"))
        marks.append(num)
        j+=1
    i+=1
dictionary = dict(zip(students, marks))
print(dictionary)

