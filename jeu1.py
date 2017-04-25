import random

nb_mystere = random.randrange(1,100)

counter = 0
counter_list = []
while True:
    choix = int(input("Saisissez un NB entre 1 et 100 : "))
    counter_list.append(choix)
    counter += 1
    if choix == nb_mystere:
        print("Bravo ! tu as trouvé le nombre mystère en %s coups !" % counter)
        print("[LISTE]Bravo ! tu as trouvé le nombre mystère en %s coups !" % len(counter_list))
        exit(0)
    else:
        if nb_mystere > choix:
            print("Le nombre mystère est plus grand ;)")
        else:
            print("Le nombre mystère est plus petit ;)")