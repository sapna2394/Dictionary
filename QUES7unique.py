d1=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
l1=[]
for i in d1:
    for x,y in i.items():
        if y not in l1:
            l1.append(y)
print (l1)



# c={}
# for i in d1:
#     c.update(i)
# a=[]
# for i in c.values():
#     if i not in a:
#         a.append(i)
# print(a)            