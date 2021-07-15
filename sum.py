my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
max1=0
max2=2
max3=0
list1=[]
for i in my_dict.values():
    list1.append(i)
j=0
while j<len(list1):
    if list1[j]>max1:
        max2=max1
        max1=list1[j]
    if max1>list1[j]and max2<list1[j]:
        max2=max3
        max2=list1[j]
        if max3<max2 and max3<max1:
            max3=list1[j]
            max3=max2
    j+=1
print(max1,max2,max3)