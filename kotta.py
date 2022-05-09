'''
this program contains two functions: 
    fibonacci(n):   generate fibonacci number at index n (helper function)
    kotta():        the kotta pseudo-random number algorithm (main function)
'''
from cmath import sqrt
import random 

# step 3 
def fibonacci(n: int) -> int:  
    '''
    returns fibonacci number at index (n - 1), start counting from 0

    parameter: 
        n: index of the fibonacci number 
    
    outputs: 
        fibonacci number at index n 
    '''
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def kotta():
    '''
    the kotta algorithm to generate pseudo-random number  

    parameters: 
        none
    
    outputs: 
        random-looking sequence, whose size is the input value n from user 
    '''
    # step 1
    a = 5 
    c = 1
    m = 2**3 # when done use m = 2 ** 32 or m = 2 ** 64 instead
    # step 2  
    n = eval(input("Enter sample size: "))
    # step 3 
    f = [fibonacci(i) for i in range(n)]
    print(f"Fibonacci sequence: {f}")
    # step 4
    x = [0] * n
    x[0] = random.randint(0, n + 1) # WHAT SHOULD BE THE RANGE OF RANDINT? 
    # step 5
    for i in range(1, n - 1):
        x[i + 1] = (a * x[i] + c + int(f[i]/x[0])) % m 
    # step 6
    print(f"random sequence: {x}")
    # step 7 
    x1 = x.copy()
    x1.sort()
    if (n + 1) % 2 == 0: 
        median = (x1[(n + 1)/2] + x1[((n + 1)/ 2) + 1]) / 2 # INDEX IS NOT INT
    elif (n + 1) % 2 == 1: 
        median = x1[((n + 1) + 1)/ 2] # INDEX IS NOT INT
    # step 8 & 9
    lu = []
    for i in x: 
        if i < median: 
            lu.append('l')
        if i >= median: 
            lu.append('u')
    # step 10
    # differences + 1 = number of runs in the string
    R = 1 
    # step 11 
    for i in range(1, len(lu)):
        if lu[i] != lu[i - 1]:
            R = R + 1
    # step 12 
    # Mean E(R) = ((n + 1) + 2)/2
    mean = ((n + 1) + 2) / 2
    # Variance Var(R) = (n + 1)((n + 1) − 2)/4((n + 1) − 1)
    variance = ((n + 1) * ((n + 1) - 2)) / (4 * ((n + 1) - 1))
    # Calculate Z = [R − E(R)]/ sqrt(Var(R) under H0
    # Z ∼ N(0, 1) for n(> 25)
    Z = (R - mean) / (sqrt(variance))
    # step 13 check if |Z| < 1.96
    absZ = abs(Z) 
    print(absZ)

kotta()
