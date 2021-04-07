from random import randint
import numpy as np

def get_universal_hash(m, p=104729):
    p = get_random_prime(m)
    if p < m:
        raise ValueError("p must be >= m!")
    a, b = randint(1, p), randint(0, p)
    assert a != 0
    return lambda x: ((a*x + b) % p) % m


"""
inefficient prime finding code
"""

def isPrime(x):
    for i in range(2, int(np.sqrt(x))):
        if x % i == 0:
            return False
    return True

def get_random_prime(m):
    m = max(4,m)
    # ~log(4m)/4m primes in range(m+1,5m)
    x=2
    while not isPrime(x):
        x = np.random.randint(m+1,5*m)
    return x
