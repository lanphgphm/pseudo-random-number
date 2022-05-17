def linear_congruential():  
    '''
    a :     int multiplier  (0 < a < m)
    c :     int increment   (0 <= c < m)
    m :     int modulo      (m > 0)
    x[0]:   int seed        (0 <= x[0] < m)
    n :     int size of the output sequence 
    x :     the output sequence
    '''
    a = 5 
    c = 1 
    m = 2**32 # output range # consider taking user input for this
    n = eval(input("enter size of sequence: "))
    x = [0] * n
    x[0] = eval(input("enter seed value (cannot be 0): "))
    for i in range(1, n - 1): 
        x[i + 1] = (a * x[i] + c) % m 
    print(x)
    return x

linear_congruential()