my_dict={'bijender':45,'deepak':30,'param':20,'anjili':30,'roshini':50,}
new_dict={}
length=len(my_dict)
# print(length)
for i in range(length):
    max_1=0
    for value in my_dict:
        if max_1 < my_dict[value]:
            max_1 = my_dict[value]
            key=value
    new_dict.update({key:max_1})
    my_dict.pop(key)
print(new_dict)  


# for j in range(length):
#     max_2=my_dict[0]
#     for keys in my_dict:
#         if max_2 > my_dict[keys]:
#             max_2=   



# my_dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50,'sona':1}
# dict={}
# for i in my_dict:
#     print("key - ",i,":","value - ",my_dict[i])
#     s=my_dict[i]
#     for j in my_dict:
#         a=my_dict[j]
#         if s>a:
#             dict[j]=a
# print(dict)


# for i in my_dict:
#     s=my_dict[i]
#     for j in my_dict:
#         a=my_dict[j]
#         if s<a:
#             dict[j]=a
# print(dict)                        
                        
# dict1={}
# my_dict={'sapna':10}
