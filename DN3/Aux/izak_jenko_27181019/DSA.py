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


# (p, q, g, y, x) = generate_key()
# (r, s) = sign('x', p, q, g, x)
# print(authenticate('x', r,s, p,q,g,y))


# def sign(x, p, q, alpha, a):
#     assert isinstance(x, str)

#     k = random.randint(1, q - 1)
#     gamma = pow(alpha, k, p) % q
#     h = int(sha1(x.encode('utf-8')).hexdigest(), 16)
#     delta = (euclid(k, q)[1] * (h + a*gamma)) % q

#     if gamma == 0 or delta == 0:
#         sign(x, p, q, alpha, a)
    
#     return gamma, delta

# def authenticate(x, signature, public_key):
#     gamma, delta = signature
#     (p, q, alpha, beta) = public_key
#     w = euclid(delta, q)[1]
#     h = int(sha1(x.encode('utf-8')).hexdigest(), 16)
#     e1 = (h * w) % q
#     e2 = (gamma * w) % q
#     return (gamma % q) == ((pow(alpha, e1, p) * pow(beta, e2, p) % p) % q)

# (p, q, g, y, x) = generate_key()
# (r, s) = sign('x', p, q, g, x)
# print(authenticate('x', (r,s), (p,q,g,y)))