liste_animaux = [ 'lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithorynque' ]

print("Liste animaux : ", liste_animaux)

print("liste inversée : ",liste_animaux[::-1])
print("liste inversée 2nd méthode: ", reversed(liste_animaux))

#liste_sort = liste_animaux.sort()
print("liste triée : ", sorted(liste_animaux))

liste_animaux_domestiques = [ 'chat', 'chien', 'chiot']
liste_animaux.append("troll")

for animal in liste_animaux_domestiques:
    liste_animaux.remove(animal)

print("Liste animaux : ", liste_animaux)

for animal in sorted(liste_animaux):
    print("%s comporte %s caractères" % (animal,len(animal)))