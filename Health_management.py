# This is Program for maintainig a persons's Diet and Excercise
def getdate():
    import datetime
    return datetime.datetime.now()

def diet():
    with open(f"{NAME}"+"_diet.txt") as D1 :
            print(D1.read()) 

def Exer():
    with open(f"{NAME}"+"_exer.txt") as E1:
        print (E1.read())

while True :
    Option= input("\n Press 1 for Loging \n or    2 for Retriving : \n")

#--------------------------------------Loging Data------------------------------------
#--------------------------------------For Harry-----------------------------------------

    if int(Option) == 1:
        Name= input("\n Press 1 for HARRY \n       2 for ROHAN \n or    3 for HAMMAD : \n")
        if int(Name)==1:
            Option2= input("\n Press 1 for  Diet \n or    2 for  Exercise : \n")
            if int(Option2)==1:
                with open("HARRY_diet.txt","a") as D1:
                    data=input("Your Diet :\n ")
                    D1.write(str([str(getdate())])+ " : "+ data + "\n")
                print("Your Data is Added Sucessfully...\n")
                
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break

            elif int(Option2)==2:
                with open("HARRY_Exer.txt", "a") as E1: 
                    data=input("Your Exercise :\n ")
                    E1.write(str([str(getdate())])+ " : "+ data + "\n")
                print("Your Data is Added Sucessfully...\n")
                
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break

            else:
                print(" Invalid Input \n Please Try Again...")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
                    
#--------------------------------------For Rohan-----------------------------------------      
        elif int(Name)==2:

            Option2= input("\n Press 1 for  Diet \n or    2 for  Exercise : ")

            if int(Option2)==1:
                with open("ROHAN_diet.txt","a") as D1:
                    data=input("Your Diet :\n ")
                    D1.write(str([str(getdate())])+ " : "+ data + "\n")
                print("Your Data is Added Sucessfully...\n")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
                
            elif int(Option2)==2:
                with open("ROHAN_exer.txt", "a") as E2:
                    data=input("\n Your Exercise : \n")
                    E2.write(str([str(getdate())])+ " : "+ data + "\n")
                print(" \n Your Data is Added Sucessfully...")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
                    
            else:
                print(" Invalid Input \n Please Try Again...")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
#--------------------------------------For Hummad-----------------------------------------
        elif int(Name)==3:

            Option2= input("\n Press 1 for Diet \n or    2 for  Exercise : ")

            if int(Option2)==1:
                with open("HAMMAD_diet.txt","a") as D1:
                    data=input("Your Diet :\n ")
                    D1.write(str([str(getdate())])+ " : "+ data + "\n")
                print("Your Data is Added Sucessfully...\n")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
                    
            elif int(Option2)==2:
                with open("HAMMAD_exer.txt", "a") as E3:
                    data=input("\n Your Excersise : \n")
                    E3.write(str([str(getdate())])+ " : "+ data + "\n")
                print("\n Your Data is Added Sucessfully...")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
                    
            else:
                print(" Invalid Input \n Please Try Again...")
                 
                u= input("\n Type Y for Continue : ").capitalize()
                if u == "Y":
                    continue
                else:
                    print("\n Thanks For Using Our Program")
                    break
#-------------------------------Retriving Data-------------------------------------------
    elif int(Option)==2:
        NAME=input("Your Name : \n ")
        Option2= input("\n Press 1 for  Diet \n or    2 for  Exercise : \n")
        if int(Option2)==1:
            diet()
            u= input("\n Type Y for Continue : ").capitalize()
            if u == "Y":
                continue
            else:
                print("\n Thanks For Using Our Program")
                break
        elif int(Option2)==2:
            Exer()
            u= input("\n Type Y for Continue : ").capitalize()
            if u == "Y":
                continue
            else:
                print("\n Thanks For Using Our Program")
                break   