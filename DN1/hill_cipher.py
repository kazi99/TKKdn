# 2. naloga
# Hillova šifra


alphabet = "abcdefghijklmnopqrstuvwxyz"
N = len(alphabet)

to_num = {l : i for (l,i) in zip(list(alphabet),range(N))}
to_char = alphabet

def matrix_multipy(A, v):
    """ zmnoži matriko A z vektorjem v (mod N) """
    u = []
    for j in range(len(A)):
        a = 0
        for i in range(len(v)):
            a += v[i] * A[j][i] % N
        u.append(a % N)
    return u

def euclid_algo(a, n):
    """ izračuna inverz a v karakteristiki n, če ta obstaja """
    pass
    

def inverse(A):
    """ izračuna inverz 2 x 2 matrike (mod 25) """
    invA = [[A[2][2], -A[1][2] % N], [-A[2][1] % N, A[1][1]]]
    inv_detA = euclid_algo(A[1][1]*A[2][2] - A[2][1]*A[1][2] % N, N)
    return [[inv_detA * a % N for a in row] for row in invA]


def encrypt(b, k):
    """ b je besedilo dolžine, katere faktor je dimenzija matrike k. Za matriko k predpostavljamo, da je dimenzij 2 x 2 katere determinanta je obrnljiva (mod N), predstavljena kot seznam dveh seznamov. """
    c = ""
    for i in range(0, len(b), 2):
        block = matrix_multipy(k, [to_num[b[i]], to_num[b[i+1]]])
        c += [to_char[i] for i in block]
    return c

def decrypt(c, k):
    b = ""
    k_inv = inverse(k)
    for i in range(0, len(c), 2):
        block = matrix_multipy(k_inv, [to_num[b[i]], to_num[b[i+1]]])
        b += [to_char[i] for i in block]
    return b
