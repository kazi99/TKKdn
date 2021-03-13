# 2. naloga
# Hillova šifra


alphabet = "abcdefghijklmnopqrstuvwxyz"
N = len(alphabet)

to_num = {l : i for (l,i) in zip(list(alphabet),range(N))}
to_char = alphabet

def matrix_vect_multipy(A, v):
    """ Zmnoži matriko A z vektorjem v (mod N) """
    u = []
    for j in range(len(A)):
        a = 0
        for i in range(len(v)):
            a += v[i] * A[j][i] % N
        u.append(a % N)
    return u

def matrix_multipy(A, B):
    """ Zmnoži matriki A in B (mod N) """
    C = []
    for j in range(len(B[0])):
        C.append(matrix_vect_multipy(A, [B[i][j] for i in range(len(B))]))
    return [[C[i][j] for i in range(len(C))] for j in range(len(C[0]))]

def euclid(a, n):
    """ izvede Euclidov algoritem """
    r, r_prev = n, a
    s, s_prev = 0, 1
    t, t_prev = 1, 0
    while r > 0:
        q = r_prev // r
        r, r_prev = r_prev - q * r, r
        s, s_prev = s_prev - q * s, s
        t, t_prev = t_prev - q * t, t
    return r_prev, s_prev, t_prev
    

def inverse(A):
    """ izračuna inverz 2 x 2 matrike (mod 25), predpostavljamo, da je obrnljiva """
    auxA = [[A[1][1], -A[0][1] % N], [-A[1][0] % N, A[0][0]]]
    detA = A[0][0]*A[1][1] - A[1][0]*A[0][1] % N
    d, inv_detA, _ = euclid(detA, N)
    if d == 1:
        return [[inv_detA * a % N for a in row] for row in auxA]
    else:
        raise " Matrika ni obrnljiva! "


def encrypt(b, k):
    """ b je besedilo dolžine, katere faktor je dimenzija matrike k. Za matriko k predpostavljamo, da je dimenzij 2 x 2 katere determinanta je obrnljiva (mod N), predstavljena kot seznam dveh seznamov. """
    c = ""
    for i in range(0, len(b), 2):
        block = matrix_vect_multipy(k, [to_num[b[i]], to_num[b[i+1]]])
        for i in block:
            c += to_char[i]
    return c

def decrypt(c, k):
    b = ""
    k_inv = inverse(k)
    for i in range(0, len(c), 2):
        block = matrix_vect_multipy(k_inv, [to_num[c[i]], to_num[c[i+1]]])
        for i in block:
            b += to_char[i]
    return b

def count_pairs(c):
    """ Prešteje pojavitve vseh bigramov ki se pojavijo v kriptiranem besedilu c. """
    pairs = {}
    for i in range(len(c) - 1):
        pair = c[i: i+2]
        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1
    return sorted([(pair, pairs[pair]) for pair in pairs], key=lambda x: x[1], reverse=True)

def possible_key(c):
    """ Ugotovi možni ključ glede na frekvenco bigramov v angleški abecedi. Najpogostejša sta 'th' in nato 'he', zato za bigrama xy in zw, ki sta najpogostejša v kriptianem besedilu c, sklepamo nasldenji povezavi za kriptiranje:

    'th' -> xy

    'he' -> zw 
    """
    fst_pair = count_pairs(c)[0][0]
    x, y = fst_pair[0], fst_pair[1]
    snd_pair = count_pairs(c)[1][0]
    z, w = snd_pair[0], snd_pair[1]
    
    A = [[to_num['t'], to_num['h']], [to_num['h'], to_num['e']]]
    B = [[to_num[x], to_num[z]], [to_num[y], to_num[w]]]

    return inverse(matrix_multipy(A, inverse(B)))

text = """ffearisthemindkillerfearisthelittledeaththatbringstotalobliterationiwillfacemyfeariwillpermitittopassovermeandthroughmeandwhenithasgonepastmeiwillturntoseefearspathwherethefearhasgonetherewillbenothingonlyiwillremainpaulatreides"""


moj_test = """pjemhfeaplcqtzakhzmcnfiqsshhaeuwpxkyemhhhhmyjtiyqmvjtfnlxvuwmcmykcdtmuhzfpkwicnfiqaieqppmccqjlfdsykuugdbpvemtzhhtdggfremtzkqemuwhveaoqiukurbusmuhzhhrzvjasogembtpthhkqmcqkplnfiqhveaoqqkplzpmuhzjtprhhiyiwjfoamuhzzpmkiyptqamyzpokog"""


test = """STSQALWTCJMIJMTHNFEBWZTVJWMRNNHPMFICJFNWSZSXGWPFHHAJFBNTWZTVTHIRMRCGVRJTAFXBWDIVMFWSNSTVLXIRACANWLYSIYVPJQMQNFLNMRPXSBHMWNJTIYNSZNHPHPIMNZDRWBPPNSHMSBUJMUHZXJHMWPSQHHJBMHHMWMJTAFXBWDICVETVLXIRANXFVETVUDWUHBWHEBMBSXHMWEEEHMANWUJUWWHAWWSNWZMLJXVXHWTVJTZZICACHHJTNWWTZRHWWTIYJSSUWSNSTVLWWWWHHPNSTVSNWWIYNSSOPFHMWEWHMHHMWNJTIYNSXPCQJTOQYFPBQKHMWEWHMHHMWNACHRNWHMWBSZWSIOGIICVETVLWWWWHHXANZRVZYWXUMVWZHDJHXAANHRUQZZOUNBTZTJFNSBUUMBVZSTTLHZXNWDTZELTVPPAJWTICVETVNNHPMFVZYWXUTVXBAJSQIUWWMHHMWNACHTGCTJIRGFCGVGSBYAPQITSDWISVPPNNZMWCIRMSFRSXHMWZEENFGDVBMHSYOYJHPBHLANXNNZVOSUSANTCVTVUMPSIATHYFAHEGCSPBWKNZMFWUYFIKXBMHHMWAAZWGJJAHSSWKVJANANXFVMAFSENLHMWBLZNDHMSBUJMNALWUFRSXWDMFWSVBTHLLJTYOSQWHYAGJHDJTXNNSTVMXTVJH""".lower()


print(decrypt(test, possible_key(test)))
print(decrypt(moj_test, possible_key(moj_test)))