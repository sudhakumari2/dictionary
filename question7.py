# question 7
a=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}
]
num=[]
for i in a:
    for j in i.values():
        if j not in num:
            num.append(j)
print(num)