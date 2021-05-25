from SHA1_quasi_collision import encrypt, b1, b2
from DSA import sign, p, q, g, y, r, s, authenticate
from largePrimes import nBitRandom
import random


zadnja_vrstica_prejsnjega_veljavnega_bloka = '000000028638c06131cc62031ad8a42b523e7019'

# (p, q, g, y, x) = generate_key(pp, qq)
# r, s = sign('{} {}'.format(b1, b2), p, q, g, y, x)

row_1 = '{} {} {}'.format(b1, b2, int(encrypt('{} {}'.format(b1, b2)), 16))
row_2 = 'IzakJenko {} {}'.format(r, s)
row_3 = zadnja_vrstica_prejsnjega_veljavnega_bloka

print('BLOK','\n')
print(row_1)
print(row_2)
print(row_3)

###          Manjša skripta              ###
# izračunata hash, ki se začne s 7 ničlami #

row_4 = str(nBitRandom(32))
m = '{}\n{}\n{}\n{}'.format(row_1, row_2, row_3, row_4)

while encrypt(m)[:7] != '0000000':
    row_4 = str(nBitRandom(32))
    m = '{}\n{}\n{}\n{}'.format(row_1, row_2, row_3, row_4)

row_5 = encrypt(m)

###               konec                  ###

print(row_4)
print(row_5, '\n')


# to je javni ključ, ki spada na vrh
public_key = 'IzakJenko\n{}\n{}\n{}\n{}'.format(p, q, g, y)

print('JAVNI KLJUČ','\n')
print(public_key)