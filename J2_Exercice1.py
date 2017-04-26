import pathlib
import os.path

dossier = pathlib.Path("/stage")
ponctuation = (";", ",", ".", ":", "«", "»", "'", "—", "?", "!", "-", "(", ")",'"', "%","[","]","\n","=","#","*","+","/","\\")
stats = {}

for chemin in dossier.iterdir():
    chemin = str(chemin)

    if os.path.isfile(str(chemin)):
        print("Fichier %s:" % chemin)
        with open(chemin, 'r') as fichier:
            contenu = fichier.read().lower()

        for char in ponctuation:
            contenu=contenu.replace(char," ")

        for word in contenu.split():
            if len(word) > 2:
                if word in stats:
                    stats[word] += 1
                else:
                    stats[word] = 1

maxkey = max(stats, key=lambda key: stats[key])
print("%s occurences pour le mot %s" % (stats[maxkey],maxkey))
#print(stats)

print("\nElement à 1 occurences")
print('\n'.join(key for key in stats.keys() if stats[key] == 1))
