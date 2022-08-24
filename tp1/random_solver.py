import random
import time


def moveUp(puzzle, ind):
   if ind - 3 >= 0:
      aux = puzzle[ind - 3]
      puzzle[ind - 3] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle
   return puzzle

def moveDown(puzzle, ind):
   if ind + 3 < len(puzzle):
      aux = puzzle[ind + 3]
      puzzle[ind + 3] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle
   return puzzle

def moveLeft(puzzle, ind):
   if ind % 3 > 0:
      aux = puzzle[ind - 1]
      puzzle[ind - 1] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle
   return puzzle

def moveRight(puzzle, ind):
   if ind % 3 < 2:
      aux = puzzle[ind + 1]
      puzzle[ind + 1] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle
   return puzzle


def shuffle(puzzle, ind):
   func_list = [0,1,2,3]
   while True:
      selected_func = random.choice(func_list)
      if selected_func == 0:
         if ind - 3 >= 0:
            puzzle = moveUp(puzzle, ind)
            break
      elif selected_func == 1:
         if ind + 3 < len(puzzle):
            puzzle = moveDown(puzzle, ind)
            break
      elif selected_func == 2:
         if ind % 3 > 0:
            puzzle = moveLeft(puzzle, ind)
            break
      elif selected_func == 3:
         if ind % 3 < 2:
            puzzle = moveRight(puzzle, ind)
            break
   return puzzle


def main():
   puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   solucion = [1, 2, 3, 4, 5, 6, 7, 8, 0]

   # mezclo con 50 movimientos
   for _ in range(50):
      ind = puzzle.index(0)
      s_puzzle = shuffle(puzzle, ind)
      puzzle = s_puzzle

   # buscar solucion de forma aleatoria
   print(f'Estado inicial: {puzzle}')
   movimientos = 0
   while True:
      ind = puzzle.index(0)
      s_puzzle = shuffle(puzzle, ind)
      puzzle = s_puzzle
      movimientos += 1
      if puzzle == solucion:
         print(f'Solucion encontrada en {movimientos} movimientos')
         print(f'Estado final: {puzzle}')
         break


if __name__ == '__main__':

   # inicio el conteo de tiempo
   inicio = time.time()

   main()

   # finalizo e imprimo el tiempo de ejecucion
   final = time.time()
   print(f"Elapsed time: {final-inicio} s")
