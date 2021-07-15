numbers=[]
sq=[]
i=1
my_dic={}
while i<=5:
    num=int(input("enter a number"))
    numbers.append(num)
    c=num*num
    sq.append(c)
    i+=1
# for key in numbers:
#     for value in sq:
#         my_dic[key] =value
#         # sq.remove(value)
#         # break  
#         print(my_dic)

result=dict(zip(numbers,sq))
print(result)
