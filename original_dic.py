sub={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list=[]
for i in sub:
    j=0
    sub_dic={}
    while j<len(sub[i]):
        sub_dic["Science"]=sub["Science"][j]
        sub_dic["Language"]=sub["Language"][j]
        j+=1
        print(sub_dic)
#    list.append(sub_dic)
# print(list)

       
# dic=[
#     {"name":"sudha","id":122},
#     {"name":"kumar nayak","id":134},
#     {"name":"rahit","id":642},
#     {"name":"naveen kumar","id":342}
    
# ]
# i=0
# user=input("enter name")
# while i<len(dic):
#     for name in dic[i]:
#         if dic[i][name] ==user:
#             print(dic[i])
#     i+=1

