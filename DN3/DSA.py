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

# Z ukazom 
# (p, q, g, y, x) = generate_key(pp,qq)
# dobim javni in zasebni ključ:

# praštevilo p
p = 142961127436133355490138919563890348660854840976893213352964599239251544301337707783902342383086525288103655452924484721723793662485712143636442571460216320911039914868719609454147758510875050598705302510931641607766956115093646822742924491276245455898739266555549702781082840760937147638759773821954219429767

# praštevilo q, da q | p - 1
q = 1162255769745614450053660730222188860003339885989

# ⍺
g = 51457833430868155810741980353067136930541567239146403095054433942149184257784422647835406876590665273264284650495724284321088724589228842999117714989599747620029712414094585834383686860739024515804709236495810258379942929693147660171746017826797468032028293543765214675712835086559196655239001126904045053578

# β = ⍺^a
y = 40204942380399292553472885028247436379389572182846498060847259036240946149756252430117250819676882646595847884052961044934662771005083261506127210307185282582952441410018273165107939174455352322727968441594315828694808538145414147649710634950477521626434460782765086503055298980970977436127928293296675494378

# a
x = 1138367750070218568919204606040363059340137573856

# podpis besedila (moj kvazi-trk) '3566083232 2314639948' z javnim ključem (p, q, g, y) in zasebnim ključem x, dobim z ukazom
# sign('3566083232 2314639948', p, q, g, y, x)

(r, s) = (225566172244877609895172024413828634251990495042, 1139447446177213386930380424924444227091082537397)