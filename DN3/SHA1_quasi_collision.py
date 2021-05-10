from hashlib import sha1
import random

def encrypt(x):
    if isinstance(x,int):
        x = str(x)
    return sha1(x.encode('utf-8')).hexdigest()

def find_quasi_collision():
    d = dict()
    while True:
        x = str(random.getrandbits(32))
        hash_x = encrypt(x)[:11]
        if hash_x in d and x != d[hash_x]:
            return d[hash_x], x
            break
        else:
            d[hash_x] = x

# našli smo ta kvazi-trk
b1 = 3566083232
b2 = 2314639948

# še en
# 4273364043
# 13279963