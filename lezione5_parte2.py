class CSVFile ():
    # inizializzo l'oggetto e aggiungo l'attributo
    def __init__ (self, file, name):
        self.file = file
        #setto il nome del file
        self.name = name
    
    #metodo get_data: file come lista di liste
    def get_data(self):
        #lista vuota per salvare i dati
        my_list=[]

        #apro il file
        my_file = open('sales_lezione3.csv', 'r')

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

#estesione dell'oggetto CSVFile 
class NumericalCSVFile (CSVFile):

    # inizializzo l'oggetto
    def __init__ (self, name):
        #setto il nome del file
        self.name = name

    def get_data(self):

        #chiamo la get_data del genitore
        string_data = super().get_data()
        
        #stringa che conterrà i ddati in formato numerico
        numerical_data = []

        #ciclo su tutte le righe corrispondenti al file originale
        for string_row in string_data:

            #lista di supporto per salvare la riga in formato numerico (tranne il primo elemento)
            numerical_row = []

            #cilco su tutti gli elemnti della riga con un enumeratore: trovo così l'indice i della posizione dell'elemento nella riga
            for i, element in enumerate(string_row):

                if i == 0:
                    #il primo elemento della riga lo lasci in formato stringa
                    numerical_row.append(element)
                
                else:
                    #converto a float tutte le altre. Ma se fallisco, stampo l'errore e rompo il ciclo
                    try:
                        numerical_row.append(float(element))
                    except Exeption as e:
                        print('Errore in conversione del valore "{}" a numerico "{}"'.format(element,e))
                        break
            
            #alla fine aggiungo la riga in formato numerico alla lista "esterna", am solo se sono riuscito a processare tutti gli elementi. Controllo per la lunghezza
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
            
            return numerical_data


my_file = CSVFile('Vendite shampoo','sales_lezione3.csv')
print('Nome del file: "{}""'.format(my_file.name))
print('Dati contenuti nel file: "{}""'.format(my_file.get_data()))

my_file_numerico = NumericalCSVFile(name = 'sales_lezione3.csv')
print('Nome del file: "{}""'.format(my_file_numerico.name))
print('Dati contenuti nel file: "{}""'.format(my_file_numerico.get_data()))