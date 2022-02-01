board = [
  "A1", "A2", "A3",
  "B1", "B2", "B3",
  "C1", "C2", "C3"
]

print("Player 1 = X, Player 2 = O")
print(" ")

def print_board():
  rowA = [board[0], board[1], board[2],]
  rowB = [board[3], board[4], board[5]]
  rowC = [board[6], board[7], board[8]]

  print(rowA)
  print("     ")
  print(rowB)
  print("     ")
  print(rowC)
  print(" ")

print_board() 



def game_play():

  winner = 0
  while winner < 1:

    playerXposition = input("Player 1: What position would you like to play? ")
    print(" ")

    if playerXposition in board:
      selected = board.index(playerXposition)
      board.pop(selected)
      board.insert(selected, "X")

    print_board()

    winOptions = [
      [board[0], board[1], board[2]],
      [board[3], board[4], board[5]],
      [board[6], board[7], board[8]],

      [board[0], board[3], board[6]],
      [board[1], board[4], board[7]],
      [board[2], board[5], board[8]],

      [board[6], board[4], board[2]],
      [board[0], board[4], board[8]]
    ]

    xWin = ["X", "X", "X"]

    if xWin in winOptions:
      winner = 1
      print("Player 1 Wins!")

    #this is kind of redic. maybe use set and .issubset? 

    elif "A1" not in board and "A2" not in board and "A3" not in board and "B1" not in board and "B2" not in board and "B3" not in board and "C1"not in board and "C2" not in board and "C3" not in board:
      winner = 1
      print("Tie!")
      break

    else: 
      print("keep playing")
      print(" ")
      winner = 0

    # Player 2

    playerOposition = input("Player 2: What position would you like to play? ")
    print(" ")

    if playerOposition in board:
      selected = board.index(playerOposition)
      board.pop(selected)
      board.insert(selected, "O")

    print_board()

    oWin = ["O", "O", "O"]

    if oWin in winOptions:
      winner = 1
      print("Player 2 Wins!")

    elif "A1" not in board and "A2" not in board and "A3" not in board and "B1" not in board and "B2" not in board and "B3" not in board and "C1"not in board and "C2" not in board and "C3" not in board:
      winner = 1
      print("Tie!")
      break
      
    else: 
      print("keep playing")
      print(" ")
      winner = 0

game_play()




