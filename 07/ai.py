def tah_pocitace(pole):
    while True:
        nove_policko = randrange(1, 21)
        if pole[nove_policko-1] == "-":
            pole = tah(pole, nove_policko, 'o')
            print(pole)
            return pole
