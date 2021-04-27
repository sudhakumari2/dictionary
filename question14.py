# question 14
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sorted_values = sorted(d.values()) # Sort the values
sorted_dict = {}
for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
            sorted_dict[k] = d[k]
            break
print(sorted_dict)
