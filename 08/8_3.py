domaci_zvirata = ["pes", "kočka", "králík", "had"]

def je_zvire_v_seznamu(seznam):
    """ Zjistí, jestli se dané zvíře nachází v seznamu """
    nove_zvire = input("Jaké zvíře se nachází u tebe doma? ")
    for zvire in domaci_zvirata:
        if nove_zvire == zvire:
            return True
        else:
            return False
