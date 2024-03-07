from functools import lru_cache 

@lru_cache(maxsize=None)
def fib4(n:int) -> int:
    """Memoização automatica"""
    if n < 2:
        return n
    else:
        return fib4(n-1) + fib4(n-2)


if __name__ == "__main__":
    fib_5 = 5
    fib_50 = 12586269025
    print(fib4.__doc__)
    print(f"(fib4(5), expected) = ({fib4(5)}, {fib_5})")
    print(f"(fib4(50), expected) = ({fib4(50)}, {fib_50})")
    