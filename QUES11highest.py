my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
k=[]
for x in my_dict.values():
    k.append(x)
i=0
while i <len(k):
    j=0
    while j<len(k)-1:
        if k[j]>k[j+1]:
            k[j],k[j+1]=k[j+1],k[j]
        j=j+1
    i=i+1
# print(k)
a=k[3:]
print(a)




      