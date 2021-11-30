class CSVFile:
    # inizializzo l'oggetto e aggiungo l'attributo
    def __init__ (self, file, name):
        self.file = file
        #setto il nome del file
        self.name = name

        #provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
    
    def get_data(self):

        if not self.can_read:
            print('Errore, file non aperto o illegibile')
            #esco dalla funzione tornando "niente"
            return None

        else:
            #lista vuota per salvare i dati
            my_list=[]

            #apro il file
            my_file = open(self.name, 'r')

            #leggo il file linea per linea
            for line in my_file:

                #split di di ogni linea sulla virgola
                elemento = line.split(',')
                
                #se non sono sull'intestazione
                if elemento[0] != 'Date':
                    #aggiungo alla lista gli elementi di questa linea
                    my_list.append(elemento)
            #chiudo il file
            my_file.close()

            #ritorno la lista in cui ho salvato i dati
            return my_list


obj = CSVFile('Vendite shampoo', 'sales_lezione3.csv')
mia_lista = []
mia_lista = obj.get_data()
#stampo a schermo
print ('Nome file: {}'.format(obj.name))
print('Contenuto:')
for x in mia_lista:
    print(x)