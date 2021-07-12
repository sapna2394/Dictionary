# import json
# user=input("DO YOU WANT TO LOGIN OR SIGN UP:")
# f=open("USERDETAILS.json","r+")
# name=f.read()
# list3=[]
# main_list=[]
# dic={}
# if user=="signin":
#     username=input("ENTER THE USERNAME :")
#     print("USER NAME CONFIRMED :")
#     print()
#     print("PASWORD LENGTH SHOULD BE GRETER THAN 6,IT SHOULD CONTAIN SPECIAL CHARECTER,CAPITAL ALPHABET AND NUMERICAL") 
#     password=input("ENTER THE PASSWORD :")

#     if len(password)>6 and len(password)<10:
#         if "@" or "$" or "#" in password:
#             if not password.isupper():
#                 if not password.isdigit():
#                     password2=input("CONFIRM YOUR PASSWORD ")
#                     if password==password2:
#                         print("PASSWORD CONFIRMED")
#                     else:
#                         print("RENTERED PASSWORD IS INCORRECT")  
#                 else:
#                     print("NUMERICALS ARE NOT PRESENT")  
#             else:
#                 print("CAPITAL ALPHSABETS ARE NOT PRESENT")
#         else:
#                 ("PLEASE ADD SPECIAL CHARECTERS") 
#     else:
#         ("LENGTH SHOULD BE ATLEASTT 10")      

#     list1=["USERNAME","PASSWORD"]
#     list2=[username,password]    
#     i=0
#     while i<=1:
#         list3.append((list1[i],list2[i]))
#         i=i+1
#     dic.update(list3)
#     if username in name:
#         print("SORRY YOUR USERNAME ALREADY EXIST ")
#     else:
#         main_list.append(dic)
#         print("CONGRACTS!!!!"+username+"YOU ARE SIGNED UP SUCESSFULLY")
#         print("NOW YOU NEED TO FILL THE FOLLOWING DETAILS")
#         firstname=input("YOUR FIRST NAME") 
#         lastname=input("YOUR LAST NAME")
#         bd=input("YOUR DATE OF BIRTH")
#         gender=input("GENDER")
#         print("yoy have been successfully signin ")
#         list4=["FIRST NAME","LAST NAME","DATE OF BIRTH","GENDER"] 
#         list5=[firstname,lastname,bd,gender]
#         j=0
#         while j<len(list4):
#             list3.append((list4[j],list5[j]))
#             j=j+1
#         dic.update(list3)
#         final_dic={}
#         final_list=[]
#         final_list.append(("user",dic))
#         final_dic.update(final_list)
#         json.dump(final_dic,f,indent=2)
# if user=="login":
#     username=input("ENTER YOUR USER NAME :")
#     password=input("ENTER YOUR PASSWORD :") 
#     if (password in name) and (username in name):
#         print("CONGRACTS!!"+username+"YOU ARE LOGGED IN SUCCESFULLY") 
#         print("HERE ARE YOUR DETAILS :")
#         with open("userdetails.json")as f:
#             x=json.load(f)
#             for z in x.values():
#                 for u in z:
#                     print(u,":",z[u])
#     else:
#         print("ID DOES NOT EXIST!!!!")   
#         new=input("DO YOU WANT TO SING IN :") 
#         f=open("USERDETAILS.json","r+")
#         name=f.read()
#         list3=[]
#         main_list=[]
#         dic={}
#         i=0
#         while i<=1:
#             if i==1:
#                 break         
#             if new=="yes":
#                 username=input("ENTER THE USERNAME :")
#                 print("USER NAME CONFIRMED !!!!")
#                 print("PASWORD LENGTH SHOULD BE GRETER THAN 6,IT SHOULD CONTAIN SPECIAL CHARECTER,CAPITAL ALPHABET AND NUMERICAL")
#                 password=input("ENTER THE PASSWORD :")
#                 if len(password)>6 and len(password)<10:
#                     if "@" or "$" or "#" in password:
#                         if not password.isupper():
#                             if not password.isdigit():
#                                 password2=input("CONFIRM YOUR PASSWORD ")
#                                 if password==password2:
#                                     print("PASSWORD CONFIRMED")
#                                 else:
#                                     print("RENTERED PASSWORD IS INCORRECT")  
#                                     break
#                             else:
#                                 print("NUMERICALS ARE NOT PRESENT") 
#                                 break 
#                         else:
#                             print("CAPITAL ALPHABETS ARE NOT PRESENT")
#                             break
#                     else:
#                             ("PLEASE ADD SPECIAL CHARECTERS") 
#                             break
#                 else:
#                     ("LENGTH SHOULD BE ATLEASTT 10") 
#                     break     

#                 list1=["USERNAME","PASSWORD"]
#                 list2=[username,password]    
#                 i=0
#                 while i<=1:
#                     list3.append((list1[i],list2[i]))
#                     i=i+1
#                 dic.update(list3)
#                 if username in name:
#                     print("SORRY YOUR USERNAME ALREADY EXIST ")
#                 else:
#                     main_list.append(dic)
#                     print("CONGRATS!!!!"+username+"YOU ARE SIGNED UP SUCESSFULLY")
#                     print("NOW YOU NEED TO FILL THE FOLLOWING DETAILS ")
#                     firstname=input("YOUR FIRST NAME :") 
#                     lastname=input("YOUR LAST NAME :")
#                     bd=input("YOUR DATE OF BIRTH :")
#                     gender=input("GENDER :")
#                     list4=["FIRST NAME","LAST NAME","DATE OF BIRTH","GENDER"] 
#                     list5=[firstname,lastname,bd,gender]
#                     j=0
#                     while j<len(list4):
#                         list3.append((list4[j],list5[j]))
#                         j=j+1
#                     dic.update(list3)
#                     final_dic={}
#                     final_list=[]
#                     final_list.append(("user",dic))
#                     final_dic.update(final_list)
#                     json.dump(final_dic,f,indent=2)
#             if new=="no":
#                 print("AS YOU WISH!!!!!!")        

#             i=i+1 




user=input("what you want to do: if you want to signup so press 1. or if you login so press 2. \n 1.signup or 2.login: ")
if user=="1":
    user_name=input("enter user name: ")
    import json
    j=open("userdetails.json","r")
    n=j.read()
    if user_name in n:
        print("user_name already exists")
    else:
        password_1=input("enter password")
        if "#" in password_1 or "@" in password_1  :
            password_2=input("enter password again")
            if password_1==password_2:

                print("Congrats", user_name, "you are signed up success fully: ")
                Discription=input(" enter Discription : ")
                DOB=input("Date of Birth : ")
                Hobbie=input("enter your Hobbie : ")
                Gender=input("Gender Male/Female : ")
                dict={"User" : {"username" : user_name, "Password": password_1, "Profile" : {"Discription" : Discription , "DOB":DOB, "Hobbie": Hobbie , "Gender": Gender}}}
                import json
                f=open("userdetails.json", "a")
                a=json.dumps(dict)
                f.write(a)
                print()
                print(a)
                f.close()
            else:
                print("wrong password")
        else:
            print("Atleast Password should contain one special character and one number")
            print("Write password  properly")
elif user=="2":
    user_name=input("enter user name: ")
    password=input("enter password: ")
    import json
    m=open("userdetails.json","r")
    l=m.read()
    if user_name in l:
        if password in l:
            print("login successfully")
            import json
            with open("userdetails.json") as data_file:    
                data = json.load(data_file)
                users = data['User']
                for user in users:
                    count=0
                print ("users full name and password is ", users["username"] , users["Password"])
                while count<1:
                    print("profile")
                    print("Discription : ", users["Profile"]["Discription"])
                    print("DOB : ", users["Profile"]["DOB"])
                    print("Hobbie : ", users["Profile"]["Hobbie"])
                    print("Gender : ", users["Profile"]["Gender"])
                    count+=1
        else:
            print("password is incorrect")
    else:
        print("invalid User_Name")