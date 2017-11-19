domaci_zvirata = ["pes", "kočka", "králík", "had"]

def prvni_pismeno_k(seznam):
    """ Vypíše všechna zvířata, začínající na 'k' """
    for zvire in domaci_zvirata:
        if zvire[0] == "k":
            print(zvire)

prvni_pismeno_k(domaci_zvirata)
