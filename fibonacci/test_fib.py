from math import sqrt, floor
from typing import  Callable 

from fibonacci.fib2 import fib1

def fib(n):
    if n < 2: 
        return n
    else:
        return fib(n-2)+ fib(n-1)

# Testes
def test_fib():
  # Test case 1-5
  fibonacci_20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
  for i in range(0, len(fibonacci_20)): 
    assert fib(i) == fibonacci_20[i]


  assert fib(12) == floor(fibequation(12))
  assert fib(25) == floor(fibequation(25))
  assert fib(30) == floor(fibequation(30))

  for i in range(20,50):
       assert fib(i) == floor(fibequation(i))

  print("All test cases pass")


def fibequation(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))



# ====================================
# Funcoes auxiliares 
# ====================================
def test_fib(fib: Callable[[int],int]):
    inicio = 20 
    fim = 30 
    for i in range(inicio,fim+1):
        assert fib(i) == floor(fibequation(i))
        print(f"Fibonacci({i}): {fib(i) }")
    print("All test cases pass")

def fibequation(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def test_fib20(fib: Callable[[int], int]):
    fibonacci_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    fibonacci_20 = fibonacci_10 + [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    j  = 0
    for i in range(j,j+20):
        n = fib(i)
        # print(f"{n}, ", end=" ")
        print(f"[{fibonacci_20[i]:5}:  {n:5}], ", end=" ")
        if i % 4 == 0:
            print()
    print(f"Fibonacci({i}): {n}")

    

def main():
    test_fib20(fib2)
    test_fib(fib2)
    


def main():
  print("lucas")
  j = 10
  for i in range(0,j):
      n = fib(i)
      fib_eq = fibequation(i)
      # print(f"{n}, ", end=" ")
      print(f"{i:2}: {n:.2f}, {fib_eq:.2f}, ")

    
if __name__ == "__main__":
    main()