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

mia_lista = []
obj = CSVFile('Vendite shampoo', 'sales_lezione3.csv')
mia_lista = obj.get_data()
print ('Nome file: {}'.format(obj.name))
print('Contenuto:')
for x in mia_lista:
    #print("['{}','{}']".format(x[0],x[1]))
    print(x)

        

