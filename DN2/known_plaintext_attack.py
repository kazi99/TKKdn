import sys
from geffe import to_binary, lfsr, geffe, decrypt, to_plain_text

poly = (
    [1, 0, 1, 0, 0, 1], 
    [1, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    )

key_length = tuple(len(p) - 1 for p in poly)

# p1 = [1, 0, 1, 0, 0, 1]
# p2 = [1, 1, 0, 0, 0, 0, 0, 1]
# p3 = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

def index_of_coincidence(text1,text2):
    assert len(text1) == len(text2)

    counter = 0
    for (t1, t2) in zip(text1,text2):
        if t1 == t2:
            counter += 1
    return counter / len(text1)


def find_matching_key(i, z):
    for k in range(2**key_length[i] - 1):
        k = f'{k:0b}'.zfill(key_length[i])
        lfsr1 = lfsr(poly[i], k)

        y = ''.join(str(next(lfsr1)) for _ in range(len(z)))

        if index_of_coincidence(y, z) >= 0.75:
            return k


def known_plaintext_attack(plaintext, ciphertext):
    """ plaintext, ciphertext ... podana kot stringa bitov iste dolžine. \n
        Ta funkcija poišče ključ ki povezuje kriptogram in besedilo na osnovi korelacijskega napada.
    """
    n = len(plaintext)

    assert n == len(ciphertext)

    z = '{0:0b}'.format(int(plaintext, 2) ^ int(ciphertext, 2)).zfill(n)

    fst_key = find_matching_key(0, z)
    trd_key = find_matching_key(2, z)
  
    for k in range(2**key_length[1] - 1):
        k = f'{k:0b}'.zfill(key_length[1])

        g = geffe(
            lfsr(poly[0], fst_key),
            lfsr(poly[1], k),
            lfsr(poly[2], trd_key)
            )

        y = ''.join(str(next(g)) for _ in range(n))

        if z == y:
            return fst_key, k, trd_key

##### SKRIPTA #####

known_plaintext = to_binary('CRYPTOGRAPHY')

ciphertext = sys.stdin.read()

key = known_plaintext_attack(known_plaintext, ciphertext[:len(known_plaintext)])

# plaintext = '000101000111000011111001101110001101000100000011110011111000'
# ciphertext = '011001110111111110011000111110101010111001111011000111111001'

print(to_plain_text(decrypt(ciphertext, key, poly)))