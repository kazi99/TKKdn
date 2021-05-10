# Ta skripta je prirejena po https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/ [ogled 10.5.2021 18:30]

import random

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97, 101, 103,
                    107, 109, 113, 127, 131, 137, 139,
                    149, 151, 157, 163, 167, 173, 179,
                    181, 191, 193, 197, 199, 211, 223,
                    227, 229, 233, 239, 241, 251, 257,
                    263, 269, 271, 277, 281, 283, 293,
                    307, 311, 313, 317, 331, 337, 347, 349]

def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)

def getLowLevelPrime(n):
    '''Generate a prime candidate divisible by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)

        # Test divisibility by pre-generated primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc

def isMillerRabinPassed(mrc, numberOfRabinTrials=20):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True

def n_bit_prime(n):
    while True:
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            break
    return prime_candidate

def prime_p(q):
    """ Generira 1024-bitno praštevilo p, za katero velja q | p - 1. """
    for t in range(2**864, 2**865):
        if isMillerRabinPassed(t * q + 1, 50):
            return t * q + 1

def euclid(a, n):
    """ izvede Euclidov algoritem """
    r, r_prev = n, a
    s, s_prev = 0, 1
    t, t_prev = 1, 0
    while r > 0:
        q = r_prev // r
        r, r_prev = r_prev - q * r, r
        s, s_prev = s_prev - q * s, s
        t, t_prev = t_prev - q * t, t
    return r_prev, s_prev, t_prev

# To sta z veliko gotovostjo 160-bitni oz. 1024-bitni praštevili, za kateri velja q | p - 1 
qq = 1162255769745614450053660730222188860003339885989
pp = 142961127436133355490138919563890348660854840976893213352964599239251544301337707783902342383086525288103655452924484721723793662485712143636442571460216320911039914868719609454147758510875050598705302510931641607766956115093646822742924491276245455898739266555549702781082840760937147638759773821954219429767