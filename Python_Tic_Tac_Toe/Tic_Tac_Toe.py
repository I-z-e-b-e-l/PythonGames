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



def player_X_turn():

  playerXwin = 0
  while playerXwin < 1:

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
      playerXwin = 1
      print("Player 1 Wins!")
      
    else: 
      print("keep playing")
      print(" ")
      playerXwin = 0

player_X_turn()