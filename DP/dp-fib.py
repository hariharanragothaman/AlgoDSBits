def fib(n):
    first = 1
    second = 1
    third = 0
    i = 0
    print("The value is:", first)
    print("The value is:", second)

    while i < n:
        third = first + second
        print("The value is:", third)
        first = second
        second = third
        i += 1
    return third

# Bottom up  - nth fibonacci number
def fib_dp(n):
    cache = [0] * n
    cache[0] = 1
    cache[1] = 1
    print("The cache is:", cache)
    print("The value is:", cache[0])
    print("The value is:", cache[1])
    i = 2
    while i < n:
        cache[i] = cache[i-1] + cache[i-2]
        print("The value is:", cache[i])
        i += 1
    return cache[-1]

result = fib_dp(10)
print("The result is:", result)

"""
TOP - Down approach - recursion - 

fib(10) 
0 --------> 10
fib(0) - fib(1) - Fib(2)
10 ------> 0 
"""

def fib_top_down(n):
    if n <= 0:
        return n
    else:
        return fib(n-1) + fib(n-2)

"""    
       4
      / \ 
     3   2
    / \  | \
   2   1 1  0 
  / \ 
 1   0 
"""