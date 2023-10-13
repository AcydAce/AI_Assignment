def printBoard(board):
    print(board['A'] + '|' + board['B'] + '|' + board['C'])
    print('-+-+-')
    print(board['D'] + '|' + board['E'] + '|' + board['F'])
    print('-+-+-')
    print(board['G'] + '|' + board['H'] + '|' + board['I'])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True #True if space is not occupied
    else:
        return False #False if space is occupied

def insertLetter(letter, position): #inserts the specified letter ('X' or 'O') at the given position on the board
    if spaceIsFree(position):       #and then calls printBoard(board) to display the updated board.
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("It was a Draw")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Player Loses")
                exit()
            else:
                print("Player Wins")
                exit()
        return
    else:
        print("Position is occupied")
        position = input("Please enter new position:  ")
        insertLetter(letter, position)
        return

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def checkForWin():
    if (board['A'] == board['B'] and board['A'] == board['C'] and board['A'] != ' '):
        return True
    elif (board['D'] == board['E'] and board['D'] == board['F'] and board['D'] != ' '):
        return True
    elif (board['G'] == board['H'] and board['G'] == board['I'] and board['G'] != ' '):
        return True
    elif (board['A'] == board['D'] and board['A'] == board['G'] and board['A'] != ' '):
        return True
    elif (board['B'] == board['E'] and board['B'] == board['H'] and board['B'] != ' '):
        return True
    elif (board['C'] == board['F'] and board['C'] == board['I'] and board['C'] != ' '):
        return True
    elif (board['A'] == board['E'] and board['A'] == board['I'] and board['A'] != ' '):
        return True
    elif (board['G'] == board['E'] and board['G'] == board['C'] and board['G'] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if board['A'] == board['B'] and board['A'] == board['C'] and board['A'] == mark:
        return True
    elif (board['D'] == board['E'] and board['D'] == board['F'] and board['D'] == mark):
        return True
    elif (board['G'] == board['H'] and board['G'] == board['I'] and board['G'] == mark):
        return True
    elif (board['A'] == board['D'] and board['A'] == board['G'] and board['A'] == mark):
        return True
    elif (board['B'] == board['E'] and board['B'] == board['H'] and board['B'] == mark):
        return True
    elif (board['C'] == board['F'] and board['C'] == board['I'] and board['C'] == mark):
        return True
    elif (board['A'] == board['E'] and board['A'] == board['I'] and board['A'] == mark):
        return True
    elif (board['G'] == board['E'] and board['G'] == board['C'] and board['G'] == mark):
        return True
    else:
        return False

def playerMove():
    position = input("Enter the position for 'O':  ")
    insertLetter(player, position)
    return

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

board = {'A': ' ', 'B': ' ', 'C': ' ',
         'D': ' ', 'E': ' ', 'F': ' ',
         'G': ' ', 'H': ' ', 'I': ' '}

def playerMove():
    position = input("Enter the position for 'O':  ")
    insertLetter(player, position)
    print("Positions are as follows:")
    print("A, B, C")
    print("D, E, F")
    print("G, H, I")
    return


printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follows:")
print("A, B, C ")
print("D, E, F ")
print("G, H, I ")
print("\n")
player = 'O'
bot = 'X'

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()