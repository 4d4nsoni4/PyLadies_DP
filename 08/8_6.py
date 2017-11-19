domaci_zvirata = ["pes", "kočka", "králík", "had"]

def serazeni_podle_abecedy(seznam):
    """ seřadí seznam podle abecedy u druhého písmena """
    seznam.append("andulka")
    dvojice = []
    serazeny_seznam = []
    for polozka in seznam:
        dvojice.append([polozka[1:], polozka])
    for novy_seznam in sorted(dvojice):
        serazeny_seznam.append(novy_seznam[1])
    print(serazeny_seznam)

serazeni_podle_abecedy(domaci_zvirata)
