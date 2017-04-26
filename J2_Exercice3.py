import somme

print(somme.somme_3args(2,5,9))

tuple1 =( 1, 3, 3)
print(somme.somme_3args(*tuple1))

import fonctions
dictionnaire = { "k1" : "val1", "k2":"val2"}
print(fonctions.unDictionnaire(dictionnaire))

myListe = { x + 3 for x in range(0,6)}
print(myListe)

myListe = { x + 3 for x in range(0,6) if x >= 2}
print(myListe)

myListe = { x + y for x in "abc" for y in "de"}
print(sorted(myListe))

myListe = { x for x in range(0,10) }
print(somme.somme_tuple(myListe))