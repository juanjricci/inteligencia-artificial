import random
import time
import os


visitados = []


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
   func_list = [0, 1, 2, 3]
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
   # if mezclado == True:
   #    print("Se ha mezclado el puzzle con 50 movimientos")
   print(f"Estado del puzzle: {puzzle}\n")
   print("\t----------------")
   print("\t      Menu      ")
   print("\t----------------")
   print("\t0. Mezclar.")
   print("\t1. Busqueda Random.")
   print("\t2. Busqueda Bidireccional.")
   print("\t3. Busqueda por Anchura.")
   print("\t4. Salir.\n")
   selected = int(input("Selecciona una opcion: "))
   return selected


def mezclar(puzzle):
   # mezclo con 50 movimientos
   for _ in range(50):
      ind = puzzle.index(0)
      s_puzzle = shuffle(puzzle, ind)
      puzzle = s_puzzle
   mezclado = True
   return puzzle, mezclado


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
   inicio = time.time()
   #temp = []
   visitados.append(puzzle)
   print(visitados)
   movimientos = 0
   i = -1
   while 1:
      i += 1
         # if i == 5:
         #    input("Press ENTER to continue...")
         #    break
      temp = visitados[i].copy()
      ind = temp.index(0)
      print(f"Moviendo en el nodo {temp}")
      puzzleU = moveUp(temp.copy(), ind)
      if puzzleU is not None and puzzleU not in visitados:
         print(puzzleU)
         visitados.append(puzzleU)
         movimientos += 1
         if puzzleU == solucion:
            break
      puzzleD = moveDown(temp.copy(), ind)
      if puzzleD is not None and puzzleD not in visitados:
         print(puzzleD)
         visitados.append(puzzleD)
         movimientos += 1
         if puzzleD == solucion:
            break
      puzzleL = moveLeft(temp.copy(), ind)
      if puzzleL is not None and puzzleL not in visitados:
         print(puzzleL)
         visitados.append(puzzleL)
         movimientos += 1
         if puzzleL == solucion:
            break
      puzzleR = moveRight(temp.copy(), ind)
      if puzzleR is not None and puzzleR not in visitados:
         print(puzzleR)
         visitados.append(puzzleR)
         movimientos += 1
         if puzzleR == solucion:
            break
   print(f"Solucion encontrada en {movimientos} movimientos.")
   final = time.time()
   print(f"Elapsed time: {final-inicio} s")
   input("Press ENTER to continue...")


def main():
   puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   puzzle_original = puzzle
   solucion = [1, 2, 3, 4, 5, 6, 7, 8, 0]

   while True:
      selected = menu(puzzle)
      if selected == 0:
         puzzle, mezclado = mezclar(puzzle)
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
