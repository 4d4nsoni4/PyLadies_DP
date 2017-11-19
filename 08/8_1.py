domaci_zvirata = ["pes", "kočka", "králík", "had"]

def jmena_kratsi_nez_5(seznam):
    """ Vytiskne zvířata ze seznamu, jejichž počet písmen je menší 5 """
    for zvire in domaci_zvirata:
        if len(zvire) < 5:
            print(zvire)

jmena_kratsi_nez_5(domaci_zvirata)
