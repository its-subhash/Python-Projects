#Snake water Gun
import random

list1 = ["S", "W", "G"] 
Trials = 10
Computers_Point = 0
Users_Point = 0
User_Name = input ("Please Enter Your Name : ")
def Point_trials():
    print("\n Computers Point :", Computers_Point,
        "\n Users Point : ",Users_Point,
        "\n Number of Trials Remains : ", Trials)

def Computer():
        print("\n Computers choice : ", Computers_Choice)
        print("\n Computer Wins...")
        Point_trials()

def User():
    print("\n Computers choice : ", Computers_Choice)
    print("\n"+ f"{User_Name}" + " Wins...")
    Point_trials()

print("\n Type S for Snake","\n Type W for Water","\n Type G for Gun")

while True :
    while Trials != 0:
        Computers_Choice = random.choice(list1)
        Users_choice = input("\n Make Your Choice : ").capitalize()
        if Computers_Choice == Users_choice:
            print ("\n Tie... Both will get 1 points.")
            print("\n Computers choice : ", Computers_Choice)
            Computers_Point += 1
            Users_Point += 1
            Trials -= 1
            Point_trials()
        elif Computers_Choice == "S" and Users_choice == "W":
            Computers_Point += 1
            Trials -= 1
            Computer()
        elif Computers_Choice == "S" and Users_choice == "G":
            Users_Point += 1
            Trials -= 1
            User()
        elif Computers_Choice == "W" and Users_choice == "G":
            Computers_Point += 1
            Trials -= 1
            Computer()
        elif Computers_Choice == "W" and Users_choice == "S":
            Users_Point += 1
            Trials -= 1
            User()
        elif Computers_Choice == "G" and Users_choice == "S":
            Computers_Point += 1
            Trials -= 1
            Computer()
        elif Computers_Choice == "G" and Users_choice == "W":
            Users_Point += 1
            Trials -= 1
            User()
        else:
            print("\n Invalid Choice... Please Try Again")
    print("\n Results :-")
    if Computers_Point > Users_Point:
        print("\n Computer won by", Computers_Point-Users_Point, " Points.")
    elif Computers_Point < Users_Point:
        print(f"{User_Name}" + " Won by", Users_Point-Computers_Point, " Points.")
    elif Computers_Point == Users_Point:
        print("\n Great "+f"{User_Name}"+ ", Its A Tie...")
    
    choice= input("\n Type Y for playing again : ").capitalize()
    if choice == "Y":
        Trials += 10
        continue
    else:
        print("\n Thanks For Playing...")
        break