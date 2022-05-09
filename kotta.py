from cmath import sqrt
import random 

# step 3 
def fibonacci(n: int): 
    # FIBONACCI SEQUENCE GENERATED IS A LOT LONGER THAN REQUIRED 
    f1 = 0
    f2 = 1
    f = []
    for i in range(0, n+1): 
        if i == 1: 
            f.append(f1)
        if i == 2: 
            f.append(f2)
        next = f1 + f2
        f1 = f2
        f2 = next
        f.append(next)
    return f

def kotta():
    # step 1
    a = 5 
    c = 1
    m = 2 ** 32
    # step 2  
    n = eval(input("Enter sample size: "))
    # step 3 
    f = fibonacci(n)
    print(f"Fibonacci sequence: {f}")
    x = [0] * n 
    # step 4
    x[0] = random.random()
    # step 5
    for i in range(0, n - 1):
        x[i + 1] = (a * x[i] + c + int(f[i]/x[0])) % m 
    # step 6
    for i in range (0, n):
        print(x[i])
    # step 7
    # THIS PART IS NOT WORKING AS EXPECTED  
    x1 = x.copy()
    x1.sort()
    if (n + 1) % 2 == 0: 
        median = (x1[(n + 1)/2] + x1[((n + 1)/ 2) + 1]) / 2
    elif (n + 1) % 2 != 0: 
        median = x1[((n + 1) + 1)/ 2]
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
    

        


    



