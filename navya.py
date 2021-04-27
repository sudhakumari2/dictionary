a=[{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyds"}
,{"name":"jaya","score":60,"school":"pyds"},{"name":"sonam","score":60,"school":"union"}]
b={}
i=0
while i<len(a):
    b[i]=a[i]
    if a[i]["school"]=="pyds" and a[i]["scores"]>=50:
        print(b[i])
    i+=1