##This is tic tac toe gaming using min max algorithm of AI.
def analyzeboard(board):#is a function that will analyse the board and returns value
    c =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

#here c is a list of lists which contains the winning conditions of the game,there 
#are 8 winning condition in total,index 0,1,2 are horizontal ,index 3,4,5 are vertical 
#whereas 6,7 are diagonal conditions 
    for i in range(0, 8):
        if (board[c[i][0]]!=0 and
            board[c[i][0]]==board[c[i][1]] and
            board[c[i][1]]==board[c[i][2]]):
            return board[c[i][0]]#it will return the winner player 
    return 0

def constboard(board):#this function will create the  board for us 
    print("The current state of the board: \n\n")
    for i in range(0,9):
        if((i!=0)and(i%3==0)):#here we are creating the spaces,
            # by using newline after every 3 blocks
            print("\n")
        if(board[i]==0):#here it will provide blank space with "_",
            # so that it become clear for us to note whether it is filled or not
            print("_",end=" ")
        if(board[i]==-1):#this will assign "X" in the board as per player 1's move
            print("X",end=" ")
        if(board[i]==1):#this will assign "O" in the board as per player 2's move
            print("O",end=" ") 

    print("\n\n") 

def User1Turn(board):#this function is made for user 1 to do their's move 
    pos=int(input("Enter 'X'in between pos[1-9]"))
    if(board[pos-1]!=0):#checking whether the position player has entered is empty or exist inside our game
        print("Wrong Move..")
        exit(0)#this will end the game 
    board[pos-1]=-1#it will assign the player 1's move in the board 

def User2Turn(board):#this function is made for user 2 to do their's move 
      pos=int(input("Enter 'O'in between pos[1-9]"))
      if(board[pos-1]!=0):#again as done in  user1's turn checking board
        print("Wrong Move..")
        exit(0)
      board[pos-1]=1#after everything is satisfied it will assign user2's move in board

#now we wil make the main function 
def minmax(board,player):
   x=analyzeboard(board)
   if(x!=0):
      return(x*player)
   pos=-1
   value=-2
   for i in range(0,9):
       if(board[i]==0):
         board[i]=player
         score=-minmax(board,player*-1)
         board[i]=0
         if(score>value):
           value=score
           pos=i
   if(pos==-1):
       return 0
    
   return value           

def compturn(board):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
          board[i]=1
          score=-minmax(board,-1)
          board[i]=0
          if(score>value):
            value=score
            pos=i
    board[pos]=1

def main():
    choice=int(input("Enter 1 for Single Player or 2 for Multiplayer:")) 
    board=[0,0,0,0,0,0,0,0,0]#it represents the turns of the game 
    if(choice==1):
        print("Computer 'O' vs you'X':")
        player=int(input("Enter 1 to play 1st or 2 to 2nd:"))
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                break
            if((i+player)%2==0):
                compturn(board)
            else:
                constboard(board)
                User1Turn(board)    
    else:
        print("Multiplayer Game...")
        for i in range(0 ,9):
            if(analyzeboard(board)!=0):
               break     
            if(i%2==0):
              constboard(board)
              User1Turn(board)   
            else:
                constboard(board)
                User2Turn(board)
    constboard(board)     
    if(analyzeboard(board)==0):
        print("Draw..")
    elif(analyzeboard(board)==-1):
        print("Player 1 has won..") 
    elif(analyzeboard(board)==1):
        print("Player 2 has won..") 
main()               