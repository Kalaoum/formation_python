cours = 1.088535

devise = input("Devise à convertir (E/$)")

if (devise != "E") and (devise != "$"):
    print("ERROR: Devise non reconnue")
    exit(8)
else:
    valeur = float(input("Valeur à convertir : "))
    if devise == "E":
        print("%s€ => %s$" % (valeur, valeur * cours))
    else:
        print("%s$ => %s€" % (valeur, valeur / cours))