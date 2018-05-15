import numpy as np

class state:
   def __init__(self, X, Y):
      self.X = int(X)
      self.Y = int(Y)

   def matrix(self):
      board = np.matrix('0 0 0; 0 0 0; 0 0 0')
      x = 1 - self.X
      y = 1 + self.Y
      board[x,y] = 1
      return board


def main():
   """
      written in python 3
   """
   move=state(input("X: "), input("Y: "))
   print(move)

   print(move.X, move.Y)
   board = move.matrix()
   print(board)


if __name__ == '__main__':
   main()
