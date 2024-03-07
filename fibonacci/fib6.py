from typing import Generator
def fib6(n:int)-> int:
    """fib6: Gerando nros de Fibonacci com um gerador """
    yield 0                         # casos especial 
    if n > 0: yield 1               # casos especial 
    last: int = 0                   # inicialmente definido para fib(0)
    next: int = 1                   #inicialmente definido para fib(1)
    for _ in range(1,n): 
        last, next = next, last+next
        yield next

if __name__ == "__main__":
    for i in fib6(50):
        print(f"{i:10}", end=",    ")
        if i % 5 == 0:
            print()