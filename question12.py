# question 12
num1=[]
num2=[]
i=1
while i<=4:
    num=int(input("enter a number"))
    num1.append(num)
    num2.append(num*num)
    i+=1
dictionary=dict(zip(num1,num2))
print(dictionary)