my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# k=[]
# for x in my_dict:
#     k.append(x)
# i=0
# while i<len(k):
#     j=0
#     while j<len(k)-1:
#         if k[j]>k[j+1]:
#             k[j],k[j+1]=k[j+1],k[j]
#         j=j+1
#     i=i+1
# print(k)
# a=k[3:]
# print(a)


my_list=[]
my_list_key=[]
for i in range(3):
    max_1 = 0
    for value in my_dict:
        if max_1<my_dict[value]:
            max_1=my_dict[value]
            key = value
    my_list.append(max_1)
    my_list_key.append(key)
    my_dict.pop(key)
print(my_list)
print(my_list_key)
    









    