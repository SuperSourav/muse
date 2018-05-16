import numpy as np

class state:
   def __init__(self, X, Y):
      self.X = int(X)
      self.Y = int(Y)

   def matrix(self):
      self.board = np.matrix('0 0 0; 0 0 0; 0 0 0')
      x = 1 - self.X
      y = 1 + self.Y
      self.board[x,y] = 1
      return self.board

   def freepaths(self, X, Y):
      paths = [[], [], [], []]
      bonus = 0
      for i in range(3):
         if self.board[i,Y] == 1:
            bonus += 3
            break
         paths[0].append("(%i,%i)->"%(i,Y))
      for j in range(3):
         if self.board[X,j] == 1:
            bonus += 3
            break
         paths[1].append("(%i,%i)->"%(X,j))
      if (abs(X-Y) != 1):
         if ( (X+1<3 and Y+1<3) or (X-1>-1 and Y-1>-1)):
            for k in range(3):
               if self.board[k,k] == 1: 
                  bonus += 3
                  break
               paths[2].append("(%i,%i)->"%(k,k))
         if ( (X+1<3 and Y-1>-1) or (X-1>-1 and Y+1<3)):
            for l in range(3):
               if self.board[l,2-l] == 1: 
                  bonus += 3
                  break
               paths[3].append("(%i,%i)->"%(l,2-l))
      final_paths = []
      for path in paths:
         if len(path) < 3: continue
         final_paths.append("".join(path))
      if len(final_paths) == 0: bonus = 0
      return final_paths, bonus

            
        

   def probmatrix(self):
      probM = np.matrix('0 0 0; 0 0 0; 0 0 0')
      for x in range(3):
         for y in range(3):
            pathoptions, bonus = self.freepaths(x,y)
            probM[x,y] = bonus + len(pathoptions)
            print("(%i,%i): "%(x,y), pathoptions, bonus)
      return probM


def main():
   """
      written in python 3
   """
   move=state(input("X: "), input("Y: "))
   print(move)

   print(move.X, move.Y)
   board = move.matrix()
   print(board)
   Pmatrix = move.probmatrix()
   print(Pmatrix)

if __name__ == '__main__':
   main()
