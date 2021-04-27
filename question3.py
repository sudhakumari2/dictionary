# print sum of value
# my_dict = {'data1':100,'data2': -54,'data3': 247} 
# sum=0
# for x,y in my_dict.items():
#     sum=sum+y
# print(sum)

# convert list into dictionary method 1
# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,] 
# # dictionary={} 
# dictionary = dict(zip(list1, list2))
# print(dictionary) # {'a': 1, 'b': 2, 'c': 3}
# keys = ['one','two','three','four','five']
# values = [1,2,3,4,5]
#to convert list into dictionary
# res = {} 
# for key in keys: 
#     for value in values: 
#         res[key] = value 
#         values.remove(value) 
#         break  
# print ("dict : " +  str(res))
# using dictionary comprehension to convert list into dictionary
keys = ['Name','age','Contact Info']
values = ['sudha',20,'#########']   
dic = {keys[i]: values[i] for i in range(len(keys))}
print (dic)