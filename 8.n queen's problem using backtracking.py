# Author: MD.Shahdat Hossain Bhuian

from typing import List
board_cnt = 0


def IsBoardOk (chessboard : List, row : int, col : int) :
   for c in range(col) :
       if (chessboard[row][c] == 'Q') :
           return False
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (chessboard[r][c] == 'Q') :
           return False
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)) :
      if (chessboard[r][c] == 'Q') :
          return False
   return True


def DisplayBoard (chessboard : List) :
    for row in chessboard :
        print(row)


def PlaceNQueens (chessboard : List, col : int) :
    global board_cnt
    if (col >= len(chessboard)) :
        board_cnt += 1
        print("Board " + str(board_cnt))
        print("==========================")
        DisplayBoard(chessboard)
        print("==========================\n")
    else :
        for row in range(len(chessboard)) :
            chessboard[row][col] = 'Q'
            if (IsBoardOk(chessboard, row, col) == True) :
                PlaceNQueens(chessboard, col + 1)
            chessboard[row][col] = '-';
            

chessboard = []
N = int(input("Enter chessboard size : "))
for i in range(N) :
    row = ["-"] * N
    chessboard.append(row)
PlaceNQueens(chessboard, 0)