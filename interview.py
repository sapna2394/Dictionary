name=['sapna','gauri','neha']
age=[19,20,21]
a={}
b=[]
i=0
while i<len(name):
    new={"name":name[i],"age":age[i]}
    a.update(new)
    b.append(new)
    i=i+1
print(b)    


# anagram
# from collections import Counter
# def check(s1, s2):
#     if(Counter(s1) == Counter(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")
# s1 = "sagarika"
# s2 = "gsaaira"
# check(s1, s2)

# s="asagirlakp"
# t="sagalprika"
# for i in s:
#     if sorted(s)==sorted(t):
#         print("anagram")
#         break
#     else:
#         print("not anagram") 
#         break



# b=[]
# i=1
# while i<=len(t):
#     print(a[-i])
#     b.append(a[-i])
#     i=i+1
# if b==a:
#     print("anagram")
# else:
#     print("not anagram")      
# print(k)

# a="sapna"
# b="apsna"
# c=list(a)
# d=list(b)
# i=0
# while i <len(c):
#     if sorted(c)==sorted(d):
#         print("anagramm")
#         break
#     else:
#         print("not anagram")  
#         break 
#     i=i+1     
