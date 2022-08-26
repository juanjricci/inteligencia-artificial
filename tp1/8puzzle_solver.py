import random
import time
import os

from sympy import true


def moveUp(puzzle, ind):
   if ind - 3 >= 0:
      aux = puzzle[ind - 3]
      puzzle[ind - 3] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle

def moveDown(puzzle, ind):
   if ind + 3 < len(puzzle):
      aux = puzzle[ind + 3]
      puzzle[ind + 3] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle

def moveLeft(puzzle, ind):
   if ind % 3 > 0:
      aux = puzzle[ind - 1]
      puzzle[ind - 1] = puzzle[ind]
      puzzle[ind] = aux
      return puzzle

def moveRight(puzzle, ind):
   if ind % 3 < 2:
      aux = puzzle[ind + 1]
      puzzle[ind + 1] = puzzle[ind]
      puzzle[ind] = aux
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


def menu(puzzle):
   os.system('clear')
   print("8-PUZZLE SOLVER")
   print("---------------")
   print(f"Estado del puzzle: {puzzle}")
   print("---------------")
   print("-----Menu------")
   print("\t0. Mezclar.")
   print("\t1. Busqueda Random.")
   print("\t2. Busqueda Bidireccional.")
   print("\t3. Busqueda por Anchura.")
   print("\t4. Salir.")
   selected = int(input("Selecciona una opcion: "))
   return selected

def mezclar(puzzle):
   # mezclo con 50 movimientos
   for _ in range(50):
      ind = puzzle.index(0)
      s_puzzle = shuffle(puzzle, ind)
      puzzle = s_puzzle
   return puzzle

def random_solver(puzzle, solucion):
   # inicio el conteo de tiempo
   inicio = time.time()

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
   
   # finalizo e imprimo el tiempo de ejecucion
   final = time.time()
   print(f"Elapsed time: {final-inicio} s")
   input("Presione ENTER para continuar...")


def bidireccional(puzzle_original, puzzle):

   # inicio el conteo de tiempo
   inicio = time.time()

   # busqueda bidireccional
   puzzle_original = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   print(f'Estado original: {puzzle_original}')
   print(f'Estado inicial: {puzzle}')
   movimientos = 0
   while True:
      ind_o = puzzle_original.index(0)
      ind = puzzle.index(0)
      o_puzzle = shuffle(puzzle_original, ind_o)
      s_puzzle = shuffle(puzzle, ind)
      puzzle_original = o_puzzle
      puzzle = s_puzzle
      movimientos += 1
      if puzzle == puzzle_original:
         print(f'Solucion encontrada en {movimientos} movimientos')
         print(f'Estado final de la original: {puzzle_original}')
         print(f'Estado final de la inicial: {puzzle}')
         break
   input("Press ENTER to continue...")

   # finalizo e imprimo el tiempo de ejecucion
   final = time.time()
   print(f"Elapsed time: {final-inicio} s")


def anchura(puzzle, solucion):
   visitados = []
   #temp = []
   visitados.append(puzzle)
   print(visitados)
   movimientos = 0
   i = -1
   while True:
      i += 1
      print(i)
      print(visitados)
      puzzle = visitados[i]
      ind = puzzle.index(0)
      if ind - 3 >= 0:
         puzzleU = moveUp(puzzle, ind)
         movimientos += 1
         if puzzleU == solucion:
            print(f'Solucion encontrada en {movimientos} movimientos')
            input("Press ENTER to continue...")
            break
         if puzzleU not in visitados:
            visitados.append(puzzleU)
      if ind + 3 < len(puzzle):
         puzzleD = moveDown(puzzle, ind)
         movimientos += 1
         if puzzleD == solucion:
            print(f'Solucion encontrada en {movimientos} movimientos')
            input("Press ENTER to continue...")
            break
         if puzzleD not in visitados:
            visitados.append(puzzleD)
      if ind % 3 > 0:
         puzzleL = moveLeft(puzzle, ind)
         movimientos += 1
         if puzzleL == solucion:
            print(f'Solucion encontrada en {movimientos} movimientos')
            input("Press ENTER to continue...")
            break
         if puzzleL not in visitados:
            visitados.append(puzzleL)
      if ind % 3 < 2:
         puzzleR = moveRight(puzzle, ind)
         movimientos += 1
         if puzzleR == solucion:
            print(f'Solucion encontrada en {movimientos} movimientos')
            input("Press ENTER to continue...")
            break
         if puzzleR not in visitados:
            visitados.append(puzzleR)
      


def main():
   puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   puzzle_original = puzzle
   solucion = [1, 2, 3, 4, 5, 6, 7, 8, 0]

   while True:
      selected = menu(puzzle)
      if selected == 0:
         puzzle = mezclar(puzzle)
      elif selected == 1:
         random_solver(puzzle, solucion)
      elif selected == 2:
         bidireccional(puzzle_original, puzzle)
      elif selected == 3:
         anchura(puzzle, solucion)
      elif selected == 4:
         break
      else:
         print("Seleccione una opcion valida!")


if __name__ == '__main__':

   main()
