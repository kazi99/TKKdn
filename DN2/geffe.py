alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = len(alphabet)

to_num = {l : i for (l,i) in zip(list(alphabet),range(N))}
to_char = alphabet

def to_binary(plain_text):
    binary = ''
    for c in plain_text:
        binary += '{0:05b}'.format(to_num[c])
    return binary

def to_plain_text(binary):
    plain_text = ''
    for i in range(0,len(binary),5):
        plain_text += to_char[int(binary[i:i+5],2)]
    return plain_text
        

def lfsr(poly, key):
    """ poly ... seznam koeficientov polinoma \n
    key ... ključ 
    
    Oba morata biti iste dolžine

    list c = [c_0, c_1, ... , c_m] <-> polinom c_0 + c_1X + ... + c_mX^m

    lfsr vrne generator, ki generira bite glede na karakteristični polinom predstavljen s seznamom poly:
    
        z_i = c[1]z[i - 1] + c[2]z[i - 2] + ... + c[m]z[i - m] (mod 2)
    """

    m = len(key)
    assert m == len(poly) - 1

    # najprej vrne vse bite iz ključa
    for k in key:
        yield int(k)

    while True:
        next_bit = 0
        for i in range(1,m + 1):
            next_bit ^= poly[i]*int(key[m - i])

        key = key[1:] + str(next_bit)
        yield next_bit

        
def geffe(lfsr1, lfsr2, lfsr3):
    while True:
        x1 = next(lfsr1)
        x2 = next(lfsr2)
        x3 = next(lfsr3)
        yield (x1 * x2) ^ (x2 * x3) ^ x3


def encrypt(b, key, poly):
    """ b ... besedilo podano v bitih kot string \n
        key ... trojica ključev, ki so podani kot stringi bitov \n
        poly ... trojica polinomov, ki podani kot seznam koeficientov, njihove stopnje so enake dolžinam pripadajočih ključev
    """

    lfsr1 = lfsr(poly[0], key[0])
    lfsr2 = lfsr(poly[1], key[1])
    lfsr3 = lfsr(poly[2], key[2])
    g = geffe(lfsr1, lfsr2, lfsr3)

    c = ''
    for bit in b:
        c += str(int(bit) ^ next(g))
    return c

def decrypt(c, key, poly):
    # ker je +1 = -1 (mod 2) lahko uporabimo isto funkcijo
    return encrypt(c, key, poly)

