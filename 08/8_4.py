#místo 'return' mám 'print', abych viděla, co se děje, ale místo tří seznamů mi vyjde cca 40x 'None', ale úplně nevidím chybu

domaci_zvirata = ["pes", "kočka", "králík", "had", "rybička", "pavouk", "želva"]
divoka_zvirata = ["tygr", "had", "lev", "pavouk", "puma", "pes"]

def seznamy_zvirat(prvni_seznam, druhy_seznam):
    """ vrátí tři seznamy, podle výskytu jednotliých zvířat """
    spolecny_seznam = []
    pouze_domaci = []
    pouze_divoka = []
    for prvni in prvni_seznam:
        for druhy in druhy_seznam:
            if prvni == druhy:
                print(spolecny_seznam.append(prvni))
            elif prvni not in druhy_seznam:
                print(pouze_domaci.append(prvni))
            elif druhy not in prvni_seznam:
                print(pouze_divoka.append(druhy))

seznamy_zvirat(domaci_zvirata, divoka_zvirata)
