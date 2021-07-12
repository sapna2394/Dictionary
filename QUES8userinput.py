i=0
dic1={}
while i<3:
    user_name=input("enter the students name")
    num=int(input("enter the marks"))
    i=i+1
    d={user_name:num}
    dic1.update(d)
print(dic1)
