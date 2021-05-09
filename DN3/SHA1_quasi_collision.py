from hashlib import sha1
import random
import time

def encrypt(x):
    if isinstance(x,int):
        x = str(x)
    return sha1(x.encode('utf-8')).hexdigest()

t1 = time.time()

d = dict()
while True:
    x = str(random.getrandbits(32))
    hash_x = encrypt(x)[:11]
    if hash_x in d and x != d[hash_x]:
        print(d[hash_x])
        print(x)
        break
    else:
        d[hash_x] = x

t2 = time.time()
print(t2 - t1)

3566083232
2314639948