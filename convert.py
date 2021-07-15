colors={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
list1=[]
list2=[]
for i,j in colors.items():
    # print(i,j)
    list1.append(i)
    list1.append(j)
list2.append(list1)
print(list2)
