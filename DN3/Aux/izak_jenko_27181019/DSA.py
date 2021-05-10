from largePrimes import n_bit_prime, isMillerRabinPassed, euclid, prime_p, qq, pp
from hashlib import sha1
import random


def generate_key(p=None, q=None):
    """ Vrne javni ključ (p, q, ⍺, β) in zasebni ključ a. """

    if p == None or q == None:
        q = n_bit_prime(160)
        p = prime_p(q)

    h = random.randint(1, p - 1)
    g = pow(h, (p - 1)//q, p)
    while g == 1:
        h = random.getrandint(1, p)
        g = pow(h, (p - 1)//q, p)
        
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    
    return (p, q, g, y, x)


def sign(msg, p, q, g, y, x):
    """ Podpiše besedilo msg in vrne podpis kot par (ɣ, δ). """
    assert isinstance(msg, str)
    h = int(sha1(msg.encode('utf-8')).hexdigest(), 16)
    k = random.randint(1, q - 1)

    r = (pow(g, k, p) % q)
    s = (euclid(k, q)[1]*(h + x*r) % q)

    return (r,s)

def authenticate(msg, r,s, p,q,g,y):
    """ Preveri ali je podpis (r,s) besedila msg osebe z javnim ključem y res avtentičen. """
    if not (0 < r < q and 0 < s < q):
        return False

    w = euclid(s,q)[1]
    h = int(sha1(msg.encode('utf-8')).hexdigest(), 16)
    u1, u2 = (h*w % q), (r*w % q)

    return ((pow(g, u1, p) * pow(y, u2, p) % p) % q) == r