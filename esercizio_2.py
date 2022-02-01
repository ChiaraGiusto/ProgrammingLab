from datetime import datetime

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

for data in data_vendite:
    print(data.strftime('%d-%m-%Y'))

