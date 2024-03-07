
def fib5(n:int)-> int:
    """fib5: Fibonacci Simples"""
    if n ==0: return n # caso espcial
    last: int = 0 # inicialmente definido para fib(0)
    next: int = 1 #inicialmente definido para fib(1)
    for _ in range(1,n): 
        last, next = next, last+next
    return next

if __name__ == "__main__":
    fib_5 = 5
    fib_50 = 12586269025
    print(fib5.__doc__)
    print(f"(fib5(5), expected) = ({fib5(5)}, {fib_5})")
    print(f"(fib5(50), expected) = ({fib5(50)}, {fib_50})")
    