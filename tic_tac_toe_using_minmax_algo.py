##This is tic tac toe gaming using min max algorithm of AI.
def analyzeboard(board):
    c =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

 
    for i in range(0, 8):
        if (board[c[i][0]]!=0 and
            board[c[i][0]]==board[c[i][1]] and
            board[c[i][1]]==board[c[i][2]]):
            return board[c[i][0]]
    return 0

def constboard(board):
    print("The current state of the board: \n\n")
    for i in range(0,9):
        if((i!=0)and(i%3==0)):
           
            print("\n")
        if(board[i]==0):
          
            print("_",end=" ")
        if(board[i]==-1):
            print("X",end=" ")
        if(board[i]==1):
            print("O",end=" ") 

    print("\n\n") 

def User1Turn(board):
    pos=int(input("Enter 'X'in between pos[1-9]"))
    if(board[pos-1]!=0):
        print("Wrong Move..")
        exit(0)
    board[pos-1]=-1

def User2Turn(board): 
      pos=int(input("Enter 'O'in between pos[1-9]"))
      if(board[pos-1]!=0):
        print("Wrong Move..")
        exit(0)
      board[pos-1]=1


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
    board=[0,0,0,0,0,0,0,0,0]
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
