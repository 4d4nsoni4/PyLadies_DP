def tah(pole, cislo_policka, symbol):
    pole = pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
    return pole
