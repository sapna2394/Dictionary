# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum)


dict1={1:2,2:3,3:4,4:5}
sum=0
i=1
a={}
while i<len(dict1):
    a.append(dict1(i))
    sum=sum+i
print(sum)    
