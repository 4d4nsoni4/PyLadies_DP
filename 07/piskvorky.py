from random import randrange

pole = 20 * "-"

def vyhodnot(pole):
    if 'xxx' in pole:
        return "x"
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return "-"
vyhodnoceni = vyhodnot(pole)

def tah(pole, cislo_policka, symbol):
    pole = pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
    return pole

def tah_hrace(pole):
    while True:
        nove_policko = int(input("Číslo pole: "))
        if nove_policko <=0:
            print("příliš malé číslo")
        elif nove_policko > 20:
            print("moc velké číslo")
        elif pole[nove_policko-1] != '-':
            print("tady je plno")
        else:
            pole = tah(pole, nove_policko, 'x')
            print(pole)
            return pole

def piskvorky1d(pole):
    vyhodnoceni = '-'
    while vyhodnoceni == '-':
        pole = tah_hrace(pole)
        vyhodnoceni = vyhodnot(pole)
        if vyhodnoceni != '-':
            break
        pole = tah_pocitace(pole)
        vyhodnoceni = vyhodnot(pole)
        if vyhodnoceni != '-':
            break
    if vyhodnoceni == 'x':
        print("gratuluji, vyhrál jsi")
    elif vyhodnoceni == 'o':
        print("pocitač byl lepsi. štětsí budeš mít třeba příště")
    else:
        print("remíza!")

piskvorky1d(pole)
