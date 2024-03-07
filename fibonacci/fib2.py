from typing import Dict, Callable
from math import sqrt,floor

memo: Dict[int,int ] = {0:0, 1:1} # casos base
# =====================
#   Funcoes Fibonacci 
# =====================


# fib1 : classic
def fib1(n):
    if n < 2: 
        return n
    else:
        return fib1(n-2)+ fib1(n-1)

# fib2 :: memoization
def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]


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
    

if __name__ == "__main__":
    print("=" * 50)
    print("\t Fib2 : memoization")
    print("=" * 50)
    main()
