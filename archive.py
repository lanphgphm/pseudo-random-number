'''
this program contains two functions: 
    fibonacci(n):           generate fibonacci number at index n, helper to kotta()
    kotta():                the kotta algorithm in question 
    kotta_tester():         contains the necessary calculations to checks the 
                            validity / accuracy of the sequence kotta() generated 
    linear_congruential():  the linear congruential pseudo-random number generator, 
                            one of the most popular PRNGs used today 
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

    variables: 
        a, c, m:    predefined numbers, constants in the given kotta formula
        n :         number of elements wanted in the output sequence 
        f :         fibonacci sequence with n elements 
        x :         array storing the generated values / output sequence
        x1 :        a copy of x, to sort & find median 
        R :         number of runs in the LU sequence, capitalized to stay 
                    consistent with the paper 
        mean,var,Z: values used to check if the generated sequence satisfy the
                    p-value
    '''
    # step 1
    a = 5  
    c = 1
    m = 16 # when done use m = 2 ** 32 or m = 2 ** 64 instead
    # step 2 
    n = eval(input("enter size of the sequence (cannot be negative): ")) 
    # step 3 
    f = [fibonacci(i) for i in range(n)]
    # step 4
    x = [0] * n
    # choose x[0] const, kotta says use random.randint(range)
    # but we will ask user for seed value
    x[0] = eval(input("enter seed value (cannot be 0): "))
    # step 5
    for i in range(1, n - 1):
        x[i + 1] = (a * x[i] + c + int(f[i] / x[0])) % m 
    # step 6
    print(f"random sequence: {x}")
    return x, n

def kotta_tester(): 
    '''
    function to test the accuracy(?) of kotta prng.   

    parameters: 
        none
    
    outputs: 
        a boolean value indicating the validity of the output of the kotta 
        algorithm 

    variables: 
        x1 :        a copy of x, to sort & find median 
        R :         number of runs in the LU sequence, capitalized to stay 
                    consistent with the paper 
        mean,var,Z: values used to check if the generated sequence satisfy the
                    p-value
    '''
    x, n = kotta()
    # step 7 
    x1 = x.copy()
    x1.sort() 
    if (n + 1) % 2 == 0: 
        median = (x1[int((n + 1)/2)] + x1[int(((n + 1)/2)) + 1]) / 2 
    elif (n + 1) % 2 == 1: 
        median = x1[int(((n + 1) + 1)/ 2)] 
    # step 8 & 9
    lu = []
    for i in x: 
        if i < median: 
            lu.append('l')
        if i >= median: 
            lu.append('u')
    # step 10
    R = 1 # because runs = differences + 1
    # step 11 
    for i in range(1, len(lu)):
        if lu[i] != lu[i - 1]:
            R = R + 1
    # step 12 
    mean = ((n + 1) + 2) / 2
    var = ((n + 1) * ((n + 1) - 2)) / (4 * ((n + 1) - 1))
    Z = (R - mean) / (sqrt(var))
    # step 13 check if |Z| < 1.96
    absZ = abs(Z)
    if abs < 1.96: 
        return True
    return False

def linear_congruential(): 
    '''
    the linear congruential algorithm to generate pseudo-random number  

    parameters: 
        none
    
    outputs: 
        random-looking sequence, whose size is the input value n from user 

    variables: 
        a, c, m:    predefined numbers, constants in the given kotta formula
        n :         number of elements wanted in the output sequence 
        x :         array storing the generated values / output sequence 
        R :         number of runs in the LU sequence, capitalized to stay 
                    consistent with the paper 
        mean,var,Z: values used to check if the generated sequence satisfy the
                    p-value
    ''' 
    a = 5
    c = 1 
    m = 16
    n = eval(input("enter size of sequence: "))
    x = [0] * n
    x[0] = eval(input("enter seed value (cannot be 0): "))
    for i in range(1, n - 1): 
        x[i + 1] = (a * x[i] + c) % m 
    print(x)
    return x

