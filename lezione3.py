#creo un vettore che salvi il risultato
values = []

#apro il file
my_file = open('sales_lezione3.csv', 'r')
#tolgo le virgole
for line in my_file:
    elementi = line.split(',')

    #tolgo la prima riga
    if elementi[0] != 'Date':
      
      #setto gli elementi
      data=elementi[0]
      valori=elementi[1]

      #aggiungo alla lista dei valori questo valore
      values.append(float(valori))
#chiudo il file
my_file.close()

#funzione somma
def sommare(values):
    somma=0
    for item in values:
        somma=somma+item
    print("somma: {}".format(somma))

#chiamo la funzione
sommare(values)


          
