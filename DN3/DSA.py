from largePrimes import n_bit_prime, isMillerRabinPassed, euclid
from hashlib import sha1
import random

qq = 1162255769745614450053660730222188860003339885989
pp = 142961127436133355490138919563890348660854840976893213352964599239251544301337707783902342383086525288103655452924484721723793662485712143636442571460216320911039914868719609454147758510875050598705302510931641607766956115093646822742924491276245455898739266555549702781082840760937147638759773821954219429767


def generate_key(p=pp, q=qq):
    """ Vrne javni ključ (p, q, ⍺, β) in zasebni ključ a"""
    q = qq
    p = pp

    # q = n_bit_prime(160)
    # p = prime_p(q)

    h = random.randint(1,p)
    alpha = pow(h, (p - 1)//q, p)
    while alpha == 1:
        h = random.getrandint(1,p)
        alpha = pow(h, (p - 1)//q, p)
        
    a = random.randint(1,q - 1)
    
    return p, q, alpha, pow(alpha, a, p), a

def prime_p(q):
    """ Generira 1024-bitno praštevilo p, za katero velja q | p - 1. """
    for t in range(2**864, 2**865):
        if isMillerRabinPassed(t * q + 1):
            return t * q + 1

def sign(x, p, q, alpha, a):
    assert isinstance(x, str)

    k = random.randint(1, q - 1)
    gamma = pow(alpha, k, p) % q
    h = int(sha1(x.encode('utf-8')).hexdigest(), 16)
    delta = (euclid(k, q)[2] * (h + a * gamma)) % q

    if gamma == 0 or delta == 0:
        sign(x, p, q, alpha, a)
    
    return gamma, delta

def authenticate(x, signature, public_key):
    gamma, delta = signature
    (p, q, alpha, beta) = public_key
    w = euclid(delta, q)[2]
    h = int(sha1(x.encode('utf-8')).hexdigest(), 16)
    e1 = (h * w) % q
    e2 = (gamma * w) % q
    return (gamma % q) == ((pow(alpha, e1, p) * pow(beta, e2, p) % p) % q)

(p, q, alpha, beta, a) = generate_key(pp, qq)
(g, d) = sign('brokoli', p, q, alpha, a)
print(authenticate('brokoli', (g,d), (p,q,alpha,beta)))