from datetime import datetime

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
            
            #funzione strip: toglie gli spazi alla fine e inizio... 
            elemento[-1] = elemento[-1].strip()
            
            #se non sono sull'intestazione
            if elemento[0] != 'Date':
                #aggiungo alla lista gli elementi di questa linea
                my_list.append(elemento)
        #chiudo il file
        my_file.close()
        #ritorno la lista in cui ho salvato i dati
        return my_list
        
    def get_date_vendite(self):
        data_vendite = []

        #apro il file
        my_file = open('sales_lezione3.csv', 'r')
        #tolgo le virgole
        for line in my_file:
            elementi = line.split(',')

            #se non sto processando l'intestazione
            if elementi[0] != 'Date':
            
                #setto gli elementi
                data=elementi[0]
                valori=elementi[1]
                
                my_date= datetime.strptime(elementi[0], "%d-%m-%Y")
                data_vendite.append(my_date)
        #chiudo il file
        my_file.close()
        return data_vendite

    def __str__(self):
        my_file=open('sales_lezione3.csv', 'r')
        for line in my_file:
            elementi=line.split(',')
            if(elementi[0]=='Date'):
                print(elementi[0],elementi[1])
        my_file.close
        

mia_lista = []
obj = CSVFile('Vendite shampoo', 'sales_lezione3.csv')
mia_lista = obj.get_data()
print ('Nome file: {}'.format(obj.name))
print('Contenuto:')
for x in mia_lista:
    #print("['{}','{}']".format(x[0],x[1]))
    print(x)
mia_lista = obj.get_date_vendite()
for data in mia_lista:
    print(data.strftime('%d-%m-%Y'))
obj.__str__()