class Automobile:

    #metodo per inizializzare l'istanza di una classe
    def __init__(self, casa_autonomo, modello, numero_posti, targa):
        #attributi
        self.casa_autonomo = casa_autonomo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    #metodo per stampare le info associate all'istanza
    def __str__(self):
        return('autonomia: "{}"\nmodello: "{}"\nnumero posti: "{}"\ntarga: "{}"'.format(self.casa_autonomo, self.modello, self.numero_posti, self.targa))
    
    #metodo che stampa a schermo "Broom Broom"
    def parla (self):
        print('"Broom Broom"')
    
    #metodo che determina se due istante di Automobile hanno le stesse informazioni (tranne la targa)
    def confronta (self, altro):
        if (self.casa_autonomo == altro.casa_autonomo and self.modello == altro.modello and self.numero_posti == altro.numero_posti):
            print('I due oggetti hanno le stesse informazioni')
        else:
            print('I due oggetti non hanno le stesse informazioni')


primo_oggetto = Automobile(50, 500, 4, 2)
secondo_oggetto = Automobile( 50, 510, 4, 2)

stampa_info = primo_oggetto.__str__()
print('Informazioni relative al primo oggetto:')
print("{}".format(stampa_info))
stampa = primo_oggetto.parla()
confronto = primo_oggetto.confronta(secondo_oggetto)