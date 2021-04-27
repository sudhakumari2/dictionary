import json
# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)
out_file = open("myfile.json", "w")
json.dump(dict1, out_file, indent = 6)
out_file.close() 