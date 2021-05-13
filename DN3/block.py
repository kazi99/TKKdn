from SHA1_quasi_collision import encrypt, b1, b2
from DSA import sign, generate_key
from largePrimes import pp, qq, nBitRandom
import random


zadnja_vrstica_prejsnjega_bloka = '000000052fe0fe02b97e0b725e1ca95b75ab8f13'

(p, q, g, y, x) = generate_key(pp, qq)
r, s = sign('{} {}'.format(b1, b2), p, q, g, y, x)

row_1 = '{} {} {}'.format(b1, b2, int(encrypt('{} {}'.format(b1, b2)), 16))
row_2 = 'IzakJenko {} {}'.format(r, s)
row_3 = zadnja_vrstica_prejsnjega_bloka

print('BLOK','\n')
print(row_1)
print(row_2)
print(row_3)

### Manjša skripta ###
# [ bšs se lahko zakomentira, ustrezne vrednosti za row_4 in row_5 sta že izračunani spodaj ]
# poiščemo tako četrto vrstico da bo sha-1 uporabljen na prvih štirih vrsticah vrnil hash vrednost, ki se začne s sedmimi ničlami.

# row_4 = str(nBitRandom(32))
# m = '{}\n{}\n{}\n{}'.format(row_1, row_2, row_3, row_4)

# while encrypt(m)[:7] != '0000000':
#     row_4 = str(nBitRandom(32))
#     m = '{}\n{}\n{}\n{}'.format(row_1, row_2, row_3, row_4)

# row_5 = encrypt(m)

###     konec      ###


# Ti dve vrstici sem dobil iz zgornje while zanke
row_4 = '2782570156'
row_5 = '00000003a3d77fdc0f6e4492275acc8e08740f5e'

print(row_4)
print(row_5)

# to je niz ki ga sha-1 preslika v 00000003a3d77fdc0f6e4492275acc8e08740f5e
m = '3566083232 2314639948 1331457644987023306915329595383178299443741746176\nIzakJenko 1142577795190654443520389728578545917931944978949 233323764178989057792929024652847273416340521174\n000000052fe0fe02b97e0b725e1ca95b75ab8f13\n2782570156'

# to je naslednji blok v našem blockchainu (v trenutku oddaje rešitev...)
my_block = '3566083232 2314639948 1331457644987023306915329595383178299443741746176\nIzakJenko 1142577795190654443520389728578545917931944978949 233323764178989057792929024652847273416340521174\n000000052fe0fe02b97e0b725e1ca95b75ab8f13\n2782570156\n00000003a3d77fdc0f6e4492275acc8e08740f5e'

# to je javni ključ, ki spada na vrh
public_key = 'IzakJenko\n{}\n{}\n{}\n{}'.format(p, q, g, y)