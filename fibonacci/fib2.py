import time 
from typing import Dict
memo: Dict[int,int ] = {0:0, 1:1} # casos base
"""
Utiliza a tecnica de Memoization
 """
def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


if __name__ == "__main__":
    j = 10
    for i in range(0,j):
        n = fib(i)
        # print(f"{n}, ", end=" ")
        print(f"{i}: {n}, ", end=" ")
