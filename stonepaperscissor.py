import random
Coptions,Uoptions=['Rock','Paper','Scissor'],{'R':'Rock','P':'Paper','S':'Scissor'}
Tries,Cpoints,Upoints=[10,0,0]
def Computerwins(computer,tries,cpoints):
    print(f"Computer Chose {computer}, Computer wins this point.")
    tries-=1
    cpoints+=1
    return tries,cpoints
while Tries>0:
    try:
        User=input(f"\nYou have {Tries} left,\nR for Rock\nP for Paper\nS for Scissor\nEnter: ").upper()
        Computer=random.choice(Coptions)      
        if Uoptions[User] == Computer:
            print(f"Computer also Chose {Computer} so its Draw, No Points to Anyone.")
            Tries-=1
        elif Computer==Uoptions['R'] and Uoptions[User]=='Scissor':
            Tries,Cpoints=Computerwins(Computer,Tries,Cpoints)
        elif Computer==Uoptions['P'] and Uoptions[User]=='Rock':
            Tries,Cpoints=Computerwins(Computer,Tries,Cpoints)
        elif Computer==Uoptions['S'] and Uoptions[User]=='Paper':
            Tries,Cpoints=Computerwins(Computer,Tries,Cpoints)
        else:
            print(f"Computer Chose {Computer}, You wins this point.")
            Tries-=1
            Upoints+=1
    except Exception:
        print("You selected worng option, hence one point to Computer.")
        Cpoints+=1
        Tries-=1
if Cpoints > Upoints:
    print(f"\nEnd Result:\nYou     : {Upoints}\nComputer: {Cpoints}\nComputer Won by {Cpoints-Upoints} points.")
elif Cpoints < Upoints:
    print(f"\nEnd Result:\nYou     : {Upoints}\nComputer: {Cpoints}\nYou Won by {Upoints-Cpoints} points.")
else:
    print(f"\nEnd Result:\nYou     : {Upoints}\nComputer: {Cpoints}\nIts a Draw")