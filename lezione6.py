class CSVFile ():
    # inizializzo l'oggetto e aggiungo l'attributo
    def __init__ (self, name):
        #setto il nome del file
        self.name = name
        
        #alzo l'eccezione se il nome del file non è una stringa
        #if name != type(str):
            #raise Exception ('Il nome del file non è una stringa!')
    
    def get_data(self, start=None, end=None):
        #lista vuota per salvare i dati
        my_list=[]

        #apro il file
        my_file = open('sales_lezione3.csv', 'r')
        
        #leggo il file linea per linea
        for elemento in my_file:
            #leggo solo dalla riga 1 alla 10
            #if start and end in [my_file]:
            for line in range(start,end):
                my_file.read()
            

            #split di di ogni linea sulla virgola
            #elemento = line.split(',')

            #funzione strip
            #elemento[-1] = elemento[-1].strip()
            
            #se non sono sull'intestazione
            if elemento[0] != 'Date':
                #aggiungo alla lista gli elementi di questa linea
                my_list.append(elemento)
        #chiudo il file
        my_file.close()

        #ritorno la lista in cui ho salvato i dati
        return my_list


my_file = CSVFile(name='sales_lezione3.csv')
print('Nome del file: "{}""'.format(my_file.name))
print('Dati contenuti nel file: "{}""'.format(my_file.get_data(start=2, end=10)))