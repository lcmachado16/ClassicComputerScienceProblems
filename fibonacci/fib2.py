import time 

#fib2

def fib2(n):
    """fib1: fibonacci Classico """
    if n < 2: 
        return n
    else:
        return fib2(n-2)+ fib2(n-1)
    

def main():
    fib1onacci_20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    inicio = 0 
    fim = 20
    print("=" * 50)
    print(fib2.__doc__)

    for i in range(inicio,fim+1):
        n = fib2(i)
        # print(f"{n}, ", end=" ")
        print(f"[fib({i:2}), expected]: [{fib1onacci_20[i]:4}:  {n:4}], ")
    print("=" * 50)
    
if __name__ == "__main__":
    main()