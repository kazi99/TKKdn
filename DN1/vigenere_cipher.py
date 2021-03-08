# 1. naloga
# Vigenerjeva šifra


alphabet = "abcdefghijklmnopqrstuvwxyz"
N = len(alphabet)

to_num = {l : i for (l,i) in zip(list(alphabet),range(N))}
to_char = alphabet

def encrypt(b, key):
    """ b je besedilo dolžine n, key pa ključ iste dolžine n """
    c = ""
    for (l,k) in zip(b,key):
        c += to_char[(to_num[l] + to_num[k]) % N]
    return c

def decrypt(c, key):
    """ c je kriptogram dolžine n, key pa ključ iste dolžine n """
    d = ""
    for (l,k) in zip(c,key):
        d += to_char[(to_num[l] - to_num[k]) % N]
    return d



def factors(n):
    f = []
    k = 2
    while k**2 < n:
        if n % k == 0:
            f.append(k)
        k += 1
    return f

def count_divisors(spacing):
    divisors = {}
    for k in spacing:
        for f in factors(k):
            if f not in divisors:
                divisors[f] = 1
            else:
                divisors[f] += 1
    
    l = [(d, divisors[d]) for d in divisors]
    return sorted(l, key=lambda x: x[1], reverse=True)

def key_lengths(c):
    """ Izpiše možne dolžine ključev oz. njihove faktorje in kako pogosto je ta ravno faktor razmika dveh zaporednih enkaih blokov v padajočem vrstnem redu. Zaenkrat preverja samo po blokih dolžine 3. """
    n = len(c)
    spacing = []
    for i in range(n-3):
        sub_string = c[i:i+3]
        j = i + 3
        while j < n - 3:
            if c[j:j+3] == sub_string:
                spacing.append(j - i)
            j += 1
    
    return count_divisors(spacing)

def likely_key_length(c):
    """ predpostavljamo, da so ključi dolžine manj kot 4 ne varni, zato izberemo najmanjšo dolžino ključa, ki je vsaj 4 in ki je hkrati tudi najpogostejša med takšnimi. """
    lengths = key_lengths(c)
    i = 0
    while lengths[i][0] < 4:
        i += 1
    return lengths[i][0]



def frequency_analysis(c): 
    L = likely_key_length(c)
    n = len(c) # dolžina kriptograma
    key = '' 
    for j in range(L):
        counter = {l : 0 for l in alphabet}
        i = 0
        while L * i  + j < n:
            counter[c[L * i + j]] += 1
            i += 1
        print(counter)

        most_freq = 'a'
        for l in counter:
            if counter[l] > counter[most_freq]:
                most_freq = l
        print(most_freq)

        # recimo, da se vedno črka "e" pojavi najpogosteje
        # zdej vemo da "e" -> most_freq

        k = to_char[(to_num[most_freq] - to_num["e"]) % N]
        key += k
        counter.clear()
    
    print(key)
    return key

#######################

text = """UTAHELHUSBXLZAZYMVXXGELAUOGDTEMOQRTUKGHCQRGTQNMUATMVASMYANZMARMOQLBIQRMPQSHMUTLWQOISQCTUNELADOGNQNHBSHMVYABUFABUUTLLJILAQNVLUNZYQAMLYEKNQNVPQSHUFHBZBOBUFTALBRXZQNMYQBXSXIHUNRHBSHMVGRKLBUUSUCMVMSXCQRXAQSMHZDMOQPKLEIWLZTBHXEELOTBVZOVJGRKPZGBUDEZBXAKJAUKZQDNYUNZATEKLNEESUOGHPDXKZOMHXIMAXEMVFHXZFRTPZTALETKPREHMFHXLXEVAUOGPEBNATUFHZNTAGRXWDAVAUCTSXYTWBLBLPTHATEYHOTLPZTALOALL""".lower()

print(key_lengths(text))
print(likely_key_length(text))
key = frequency_analysis(text)

# dobim ključ "maih", pametno ugibanje nam da ključ "math".

print(decrypt(text, 93 * key))
print(decrypt(text, 93 * "math"))