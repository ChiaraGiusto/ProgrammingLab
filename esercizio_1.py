#stampa contenuto della lista
def stampa(lista):
    print("Contenuto: {}".format(lista))
#funzione statistiche
def statistiche(lista):
    somma = 0
    for item in lista:
        #verificare se è una lista di interi
        type(item) == int
        #somma
        somma = somma + item
        #media
        media = somma/len(lista)
        #minimo
        minimo = min(lista)
        #massimo
        massimo = max(lista)
    #stampa dei risultati
    print("Somma: {}".format(somma))
    print("Media: {}".format(media))
    print("Minimo: {}".format(minimo))
    print("Massimo: {}".format(massimo))
#funzione somma-vettoriale
def somma_vettoriale(lista1, lista2):
    somma_liste = 0
    lista3 = []
    #verificare che abbiano la stessa dimensione
    if len(lista1) == len(lista2):
        for i,j in zip(lista1, lista2):
            #verificare che siano due liste di interi
            type (i) == int and type (j) == int
            #somma vettoriale
            lista3.append(i + j)
    else: 
        lista3
    print("Somma vettoriale: {}".format(lista3))

#creazione della lista
my_list = [1,5,8,6,8,4]
my_list_2 = [1,5,8,6,8,4]
my_list_3 = []
stampa(my_list)
statistiche(my_list)
somma_vettoriale(my_list,my_list_2)