import time 

#fib2
"""fib1: fibonacci Classico """
def fib1(n):
    if n < 2: 
        return n
    else:
        return fib1(n-2)+ fib1(n-1)
    

def main():
    fib1onacci_20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    j  = 0
    for i in range(j,j+20):
        n = fib1(i)
        # print(f"{n}, ", end=" ")
            print(f"(fib3(5), expected) = ({fib3(5)}, {fib_5})")
        print(f"[{fib1onacci_20[i]:5}:  {n:5}], ", end=" ")
        if i % 4 == 0:
            print()
    print()
    
if __name__ == "__main__":
    main()