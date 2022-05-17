from cmath import sqrt
import random 

def fibonacci(n: int) -> int:  
    try: 
        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    except Exception as e: 
        print(f"Error message: {e}")
        return ()

def kotta():
    a = 5  
    c = 1
    m = 2**32 
    n = eval(input("enter size of the sequence (cannot be negative): ")) 
    f = [fibonacci(i) for i in range(n)]
    x = [0] * n
    # choose x[0] const, kotta says use random.randint(range)
    # but we will ask user for seed value
    x[0] = eval(input("enter seed value (cannot be 0): "))
    for i in range(0, n - 1):
        x[i + 1] = (a * x[i] + c + int(f[i] / x[0])) % m 
    print(f"random sequence: {x}")
    # checking accuracy 
    x1 = x.copy()
    x1.sort() 
    if (n + 1) % 2 == 0: 
        median = (x1[int((n + 1)/2)] + x1[int(((n + 1)/2)) + 1]) / 2 
    elif (n + 1) % 2 == 1: 
        median = x1[int(((n + 1) + 1)/ 2)] 
    lu = []
    for i in x: 
        if i < median: 
            lu.append('l')
        if i >= median: 
            lu.append('u')
    R = 1 # because runs = differences + 1
    for i in range(1, len(lu)):
        if lu[i] != lu[i - 1]:
            R = R + 1
    mean = ((n + 1) + 2) / 2
    var = ((n + 1) * ((n + 1) - 2)) / (4 * ((n + 1) - 1))
    Z = (R - mean) / (sqrt(var))
    absZ = abs(Z)
    if absZ < 1.96: 
        return True
    return False

kotta()