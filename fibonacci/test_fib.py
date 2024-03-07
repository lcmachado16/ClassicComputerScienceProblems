from math import sqrt, floor
from typing import  Callable 

from fib2 import fib2
from fib3 import fib3 
from fib4 import fib4
from fib5 import fib5
from fib6 import fib6

# ====================================
# Funcoes auxiliares 
# ====================================


#Specific tests 
def test_fib20(fib: Callable[[int], int]):
  """Testa os 20 primeiros valores da sequencia de fibonacci """
  fibonacci_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  fibonacci_20 = fibonacci_10 + [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
  inicio = 0 
  fim = 20

  print("=" * 50)
  print(fib.__doc__)
  for i in range(inicio, fim +1):
      n = fib(i)
      print(f"[{fibonacci_20[i]:5}:  {n:5}], ", end=" ")
      if i % 4 == 0:
          print()
  print(f"Fibonacci({i}): {n}")
  print("=" * 50)

def fib6_test(n):
  print("=" * n)
  print(fib6.__doc__)
  for i in fib6(n):
      print(f"{i:10}", end=",    ")
      if i % (n//10) == 0:
          print()
  print("=" * n)

#General tests 

def test_fib(fib: Callable[[int],int], inicio, fim):
    for i in range(inicio,fim+1):
        assert fib(i) == floor(fibequation(i))
        print(f"Fibonacci({i}): {fib(i) }")
    print("All test cases pass")


def fibequation(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def testes_fibs(funcoes:list[Callable[[int], int]]):
    for funcao in funcoes:
      print("=" * 50)
      print(funcao.__doc__)
      test_fib(funcao,0,20)
      print("=" * 50)

  

def main():
  test_fib20(fib2)
  
  funcoes = [fib3,fib4,fib5] 
  testes_fibs(funcoes)

  fib6_test(50)
  

if __name__ == "__main__":
    main()