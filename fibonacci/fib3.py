from typing import  Dict
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
def fib3(n: int) -> int:
    """fib3: Memoization """
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


if __name__ == "__main__":
    fib_5 = 5
    fib_50 = 12586269025
    print("=" * 50)
    print(fib3.__doc__)
    print(f"(fib3(5), expected) = ({fib3(5)}, {fib_5})")
    print(f"(fib3(50), expected) = ({fib3(50)}, {fib_50})")
    print("=" * 50)
    