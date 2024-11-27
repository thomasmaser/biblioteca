from libro import Nuovo
from libro import Prestito
from libro import Rientro
from libro import Check
continua = "si"
while (continua == "si"):
    print("selezionare il numero dell'operazione da svolgere:\n-1 aggiungere un libro al catalogo\n-2 assegnare un libro in prestito\n-3 rientro dal prestit\n-4 disponibilità libro")
    while True:
        operazione = int(input())
        if operazione == 1:
            Nuovo()
            break
        elif operazione == 2:
            Prestito()
            break
        elif operazione == 3:
            Rientro()
            break
        elif operazione == 4:
            Check()
            break
        else:
            print("selezionare un numero valido")
    continua = input("si desidera effettuare un'altra operazione?\n")