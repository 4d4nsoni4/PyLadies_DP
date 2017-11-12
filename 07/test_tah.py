#aby mi test prošel, musela jsem si vytvóřit nový soubor tah.py, kam jsem kód vložila

import tah

def test_tah():
    symbol = "x"
    cislo_policka = 3
    pole = 20*"-"
    pole = pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
    spravne_pole = 2*"-"+"x"+17*"-"

    assert pole == spravne_pole
