catalogo = ["Arancia meccanica", "Tropico del cancro", "Il vecchio e il mare", "Dune", "Il capitale"]
prestito =[]

def AddToCatalogo(libro):
    catalogo.append(libro)

def RemoveFromCatalogo(libro):
    catalogo.remove(libro)

def AddToPrestito(libro):
    prestito.append(libro)

def RemoveFromPrestito(libro):
    prestito.remove(libro)

def Nuovo():
    nuovoLibro = input("inserire il titolo del libro da aggiungere al catalogo: ")
    if nuovoLibro in catalogo or nuovoLibro in prestito:
        print("è già presente una copia di", nuovoLibro, "in catalogo")
    else:
        AddToCatalogo(nuovoLibro)
        print(nuovoLibro, "è stato aggiunto al catologo")
        print(catalogo)

def Prestito():
    while True:
        libro = input("inserire il titolo del libro: ")
        if libro in catalogo:
            RemoveFromCatalogo(libro)
            AddToPrestito(libro)
            print(libro, "è stato inserito tra i prestiti")
            print(prestito)
            break
        elif libro in prestito:
            print("il libro è già in prestito")
            break
        else:
            print("il libro non è in catalogo, desidera inserire un altro titolo?\n")
            ripeti = input()
            if ripeti == "no":
                break
            else:
                pass


def Rientro():
    while True:
        libro = input("inserire il titolo del libro: ")
        if libro in prestito:
            RemoveFromPrestito(libro)
            AddToCatalogo(libro)
            print(libro, "è stato riaggiunto al catalogo disponibili")
            print(catalogo)
            break
        elif libro in catalogo:
            print("il libro è già rientrato dal prestito")
            break
        else:
            print("il libro non è in catalogo, desidera inserire un altro titolo?\n")
            ripeti = input()
            if ripeti == "no":
                break
            else:
                pass
            


def Check():
    libro = input("inserire il titolo del libro: ")
    if libro in catalogo:
        print(libro, "è presente nel nostro catalogo e disponibile")
    elif libro in prestito:
        print(libro, "al momento è in prestito")
    else:
        print("non abbiamo questo libro in catalogo")


