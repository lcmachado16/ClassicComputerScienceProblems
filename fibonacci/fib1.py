import time 

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

  print("All test cases pass")


def main():
    fibonacci_20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    j  = 0
    for i in range(j,j+20):
        n = fib(i)
        # print(f"{n}, ", end=" ")
        print(f"[{fibonacci_20[i]:5}:  {n:5}], ", end=" ")
        if i % 4 == 0:
            print()
    print()
    
if __name__ == "__main__":

    main()