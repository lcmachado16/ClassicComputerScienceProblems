from math import sqrt

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

  assert(fib(12),fibequation(12))
  assert(fib(10),fibequation(10))


  print("All test cases pass")


def fibequation(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))



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