# dune = {"autore" : "F. Herbert", "anno" : 1973, "tipo" : "romanzo", "genere" : "fantascienza"}
# aranciaMeccanica = {"autore" : "A. Burgess", "anno" : 1962, "tipo" : "romanzo", "genere" : "fantapolitico"}
# tropicoDelCancro = {"autore" : "H. Miller", "anno" : 1934, "tipo" : "romanzo", "genere" : "narrativa autobiografica"}
# ilVecchioEIlMare = {"autore" : "E. Hemingway", "anno" : 1952, "tipo" : "romanzo", "genere" : "romanzo di formazione"}
# ilCapitale = {"autore" : "K. Marx", "anno" : 1867, "tipo" : "saggio", "genere" : "politico"}

# catalogo = {"Dune" : dune, "Arancia meccanica" : aranciaMeccanica, "Tropico del cancro" : tropicoDelCancro, "Il vecchio e il mare" : ilVecchioEIlMare, "Il capitale" : ilCapitale}
# prestito = {}

catalogo = {
    1 : {
        "titolo" : "Dune",
        "autore" : "F. Herbert", 
        "anno" : 1973, 
        "tipo" : "romanzo", 
        "genere" : "fantascienza",
    },
    2 : {
        "titolo" : "Arancia meccanica",
        "autore" : "A. Burgess", 
        "anno" : 1962, 
        "tipo" : "romanzo", 
        "genere" : "fantapolitico",
    },
    3 : {
        "titolo" : "Tropico del cancro",
        "autore" : "H. Miller", 
        "anno" : 1934, 
        "tipo" : "romanzo", 
        "genere" : "narrativa autobiografica",
    },
    4 :{
        "titolo" : "Il vecchio e il mare",
        "autore" : "E. Hemingway", 
        "anno" : 1952, 
        "tipo" : "romanzo", 
        "genere" : "romanzo di formazione"
    },
    5 : {
        "titolo" : "IL capitale",
        "autore" : "K. Marx", 
        "anno" : 1867, 
        "tipo" : "saggio", 
        "genere" : "politico"
    }
}

#c'è da correggere anche tutti gli inoput numerici mettendo il try

def Nuovo():
    codice = (len(catalogo)+1)
    #questo va corretto con un for sennò dando in prestito il primo libro poi mi sovrasvriverà l'ultimo
    catalogo.update({ codice : {
        "titolo" : "",
        "autore" : "",
        "anno" : 0,
        "tipo" : "",
        "genere" : ","
    }})
    catalogo[codice]["titolo"] = input("inserire il titolo: ")
    catalogo[codice]["autore"] = input("inserire l'autore (N. Cognome): ")
    anno = input("inserire l'anno: ")
    try:
        s = int(anno)
    except ValueError:
        s = 0000
    catalogo[codice]["anno"] = s
    catalogo[codice]["tipo"] = input("inserire il tipo: ")
    catalogo[codice]["genere"] = input("inserire il genere: ")
    print("è stato aggiunto il seguente libro\n", catalogo[codice])

def Check():
    print("si desidera effettuare la ricerca per:\n-1 titolo\n-2 autore\n-3 anno\n-4 tipo\n-5 genere\n-6 mostrare tutto il catalogo")
    scelta = int(input())
    if scelta == 1:
        titolo = input("inserire il titolo: ")
        



