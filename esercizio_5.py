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

#estendo la classe Automobile
class Transformer(Automobile):
    
    #sovrascrivo il metodo __init__
    def __init__(self, name, generazione, grado, reparto):

        self.name= name
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto
    

    #metodo che stampa le informazioni "militari" di un'istanza della classe Transformer
    def scheda_militare(self):

        print('Nome istanza Transformer: "{}"'.format(self.name))
        print('Generazione di appartenenza: "{}"'.format(self.generazione))
        print('Grado militare: "{}"'.format(self.grado))
        print('Divisione istanza: "{}"'.format(self.reparto))

#creo l'istanza
oggetto=Transformer('x', '1', 'soldato semplice', 'spionaggio')
#chiamo il metodo dell'istanza
oggetto.scheda_militare()
