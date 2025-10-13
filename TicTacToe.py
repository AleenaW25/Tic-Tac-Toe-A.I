import random
board = ["-", "-", "-", #Global variable
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None #We don't know the winner yet
gameRunning = True #Game is controlled by this loop


#Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)


#Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: ")) #Convert string to an integer
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer #We are checking to see if player's input is valid and that the spot they have chosen isn't occupied
    else:
        print("Oops, player is already in that spot!")




#Check for win or tie
def checkHorizontal(board):
    global winner #If changes are made to winner in this function, then the value of winner throughout the entire program should update the value
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[0]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board: #If there are no spaces left in the board
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
        
def checkWin():
    if checkHorizontal(board) or checkRow(board) or checkDiag(board):
        print(f"The winner is " + winner)
        gameRunning = False


#Switch the player
def switchPlayer(): #Don't need to pass anything into the function as the second player isn't going to be making any modifications to the board
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
        
#Computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
        

#Check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    checkWin()
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
