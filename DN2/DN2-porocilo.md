# Poročilo — 2. domača naloga
Glavnino naloge sestavljata dva dokumenta `geffe.py` in `known_plaintext_attack.py`. V prvem definiram vse potrebno za napad v drugem pa izvedem napad s poznanim besedilom iz prve opombe. Posebaj je shranjen še kriptogram v datoteki `ciphertext.txt`.

- - - -

`geffe.py`
Tukaj pripravim pomožne funkcije s katerimi zgradim geffejev generator. Po večini uporabljam Pythonove generatorje. Glavna funkcija je `lfsr`, ki vrne generator linearne rekurzivne šifre glede na karakterističen polinom podan kot seznam koeficientov, ki da rekurzivno zvezo, ter začetnega ključa, ki je binarni niz iste dolžine kot je stopnja karakterističnega polinoma. 

Funkcija `geffe` združi tri lfsr generatorje na predpisan način in tudi sama vrne generator.

Funkciji `encrypt` in `decrypt` s pomočjo geffejevega generatorja kriptirata oz. dekriptirata besedilo podana kot niz bitov, tako, da po komponentah po vrsti prištejeta izhodni bit geffejevega generatorja, ki je porojen s tremi začetnim karakterističnimi polinomi — vsak za en lfsr — ter trojico pripadajočih začetnih ključev. 

- - - -

`known_plaintext_attack.py`
V tem dokumentu bo izveden napad z znanim besedilom. V ta namen sem pripravil še nekaj pomožnih funkcij. 

Funkcija `index_of_coincidence` izračuna indeks koincidence med dvema besediloma, torej delež ujemanja dveh besedil. 

Funkcija `find_matching_key` je osnovana na dejstvu, da z izhodom Geffejevega generatorja izhoda LFSR1 in LFSR3 ujemata v približno treh četertinah primerov. Pregleda torej vse ključe danega lfsr generatorja in shrani tistega pri katerem je indeks koincidence vsaj tri četrtine. 

Glavna funkcija tega dokumenta je `known_plaintext_attack`, ki s pomočjo `find_matching_key` poišče pravi ključ, tako da pregleda vse ključe generatorjev LFSR1 in LFSR3. Ta napad smo že videli na vajah. 

- - - -

Napad je bil izveden na podlagi poznanega dela besedila, ki se začne z besedo CRYPTOGRAPHY. Ta beseda se v ustrezni obliki prevede v binarni niz `000101000111000011111001101110001101000100000011110011111000`.
Z začetnim kosom presreženega kriptograma iste dolžine kot je znano besedilo, tj. `011001110111111110011000111110101010111001111011000111111001`
poiščem ključ s pomočjo funkcije `known_plaintext_attack`. Ključ je trojica `(01110, 1101001, 11110011010)`, ki pripada lfsr-jem inicializiranim s trojico polinomov, ki so kot seznami prestavljeni s trojico 

```
poly = (
    [1, 0, 1, 0, 0, 1], 
    [1, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    )
``` 

S tem klučem se celoten kriptogram dekriptira v niz bitov, ki pa ga pretvorimo nazaj v angleško besedilo s funkcijo `to_plain_text` iz pomožne datoteke `geffe.py`. Celotno dekriptirano besedilo v angleščini je tedaj: 

> CRYPTOGRAPHYPRIORTOTHEMODERNAGEWASEFFECTIVELYSYNONYMOUSWITHENCRYPTIONTHECONVERSIONOFINFORMATIONFROMAREADABLESTATETOAPPARENTNONSENSETHEORIGINATOROFANENCRYPTEDMESSAGEALICESHAREDTHEDECODINGTECHNIQUENEEDEDTORECOVERTHEORIGINALINFORMATIONONLYWITHINTENDEDRECIPIENTSBOBTHEREBYPRECLUDINGUNWANTEDPERSONSEVEFROMDOINGTHESAMETHECRYPTOGRAPHYLITERATUREOFTENUSESALICEAFORTHESENDERBOBBFORTHEINTENDEDRECIPIENTANDEVEEAVESDROPPERFORTHEADVERSARYSINCETHEDEVELOPMENTOFROTORCIPHERMACHINESINWORLDWARIANDTHEADVENTOFCOMPUTERSINWORLDWARIITHEMETHODSUSEDTOCARRYOUTCRYPTOLOGYHAVEBECOMEINCREASINGLYCOMPLEXANDITSAPPLICATIONMOREWIDESPREAD  
>   

- - - -

Za uporabo skripte na točno tem primeru iz naloge je priložen ukaz
```
python3 known_plaintext_attack.py < ciphertext.txt
```
Sicer pa je potrebno zgolj zamenjati trojico poznanih karakterističnih polinomov v  `poly` in prirediti poznani del beselia v `known_plaintext`.  

- - - -

Domača naloga je dostopna tudi na mojem git-u na povezavi <https://github.com/kazi99/TKKdn>