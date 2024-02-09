def board(playerX,playerO):
    zero = "X" if playerX[0] else("O" if playerO[0] else "0")
    one  = "X" if playerX[1] else("O" if playerO[1] else "1")
    two  = "X" if playerX[2] else("O" if playerO[2] else "2")
    three= "X" if playerX[3] else("O" if playerO[3] else "3")
    four = "X" if playerX[4] else("O" if playerO[4] else "4")
    five = "X" if playerX[5] else("O" if playerO[5] else "5")
    six  = "X" if playerX[6] else("O" if playerO[6] else "6")
    seven= "X" if playerX[7] else("O" if playerO[7] else "7")
    eight= "X" if playerX[8] else("O" if playerO[8] else "8")
    print(f" {zero} | {one} | {two} ")
    print("---|---|----")
    print(f" {three} | {four} | {five} ")
    print("---|---|----")
    print(f" {six} | {seven} | {eight} ")

def winner(playerX, playerO):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if ((playerX[i[0]]+playerX[i[1]]+playerX[i[2]]) ==3):
            board (playerX, playerO)
            print("Player X won")
            return 1
        elif ((playerO[i[0]]+playerO[i[1]]+playerO[i[2]]) ==3):
            board (playerX, playerO)
            print("Player O won")
            return 0
    return -1

def doneit():
    while True:
        value=int(input("Enter Your Position : "))
        if value in done:
            print("This Place is already full...please select another one.")
            continue
        else:
            done.append(value)
            break
    return value

playerX=[0,0,0,0,0,0,0,0,0]
playerO=[0,0,0,0,0,0,0,0,0]
done=[]
turn=1 #1 for X and 0 for O
while True:
    board(playerX, playerO)
    if turn==1:
        print("X's Turn...")
        val= doneit()
        playerX[val]=1
    else:
        print("O's Turn...")
        val= doneit()
        playerO[val]=1
    win=winner(playerX, playerO)
    if win !=-1:
        print("Game over, it's a Tie...")
        break 
    turn= 1-turn