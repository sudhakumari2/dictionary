# question no 9
string=input("enter any sentence or word\n")
count={}
for i in string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("count of all character is :\n"+str(count))

