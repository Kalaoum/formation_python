def somme_tuple(tuple):
    somme = 0
    for value in tuple:
        if type(value) == int or type(value) == float:
            somme += value
    return somme

def somme_3args(a = 0, b = 0, c = 0):
    return (a + b + c)