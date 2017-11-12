#funkce tah mi nešla přivolat a musela jsem ji do kódu vložit, musí se to dělat takhle, nebo se to dá nějak udělat?

import ai

def test_tah_pocitace():
    nove_policko = 4
    pole = 20*"-"
    def tah(pole, cislo_policka, symbol):
        pole = pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
        return pole
    pole = tah(pole, nove_policko, 'o')
    spravne_pole = 3*"-"+"o"+16*"-"

    assert spravne_pole == pole
