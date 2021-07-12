# my_dict = {'data1':100,'data2': -54,'data3': 247}
# print(sum(my_dict.values()))


# def returnSum(myDict):
      
#     sum = 0
#     for i in myDict:
#         sum = sum + myDict[i]
      
#     return sum

# dict = {'data1':100,'data2': -54,'data3': 247}
# print("Sum :", returnSum(dict))



# myDict = {'x': 100, 'y':-54, 'z':247}
# print("Dictionary: ", myDict)
# total = 0

# # Print Values using get
# for i in myDict:
#     total = total + myDict[i]
    
# print("The Total Sum of Values : ", total)


# user={"maggi":10,"oil":30,"rice":75}
# a=int(input("enter the number"))
# i=0
# while i<a:
    
user={ "maggi":10,"oil":30,"sugar":40,"rice":75}
a=int(input("ENTER"))
i=0
sum =0
while i<a:
    b=input("ENTER THE MATERIAL")
    print(b,user[b])
    sum =sum +user[b]
    i=i+1    
print(sum)
