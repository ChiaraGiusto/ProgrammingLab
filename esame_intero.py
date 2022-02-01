class ExamException(Exception):
    pass

#esercitazione 1
class MovingAverage():

    def __init__(self, lunghezza):
        #definisco lunghezza come la lunghezza della finestra
        self.lunghezza = lunghezza

    def compute(self, lista):
        #creo una lista per memorizzare i risultati
        lista_risultato=[]
        n = len(lista)
        i = 0
        #prima eccezione: caso di lista vuota
        if(n == 0):
            raise ExamException('Lista vuota')
        #seconda eccezione: caso in cui la lunghezza della lista è minore della lunghezza della finestra
        if(n < self.lunghezza):
            raise ExamException('Lunghezza della lista minore della finestra')
        while (i+(self.lunghezza-1) < n):
            conta = 0
            media = 0
            somma = 0
            #finchè il contatore è minore della lunghezza della finestra
            while (conta < self.lunghezza):
                somma = somma + lista[conta + i]
                conta=conta+1
            i = i+1
            media = somma/self.lunghezza
            #aggiungo il risultato alla lista creata
            lista_risultato.append(media)
        return lista_risultato

#esercitazione 2
class Diff():

    def __init__(self, ratio):

        #eccezione: se ratio = 0
        if(ratio < 1):
            raise ExamException('Ratio pari a 0 o negativo')
        #eccezione: se ratio non è un numero
        if not (isinstance(ratio, int) or isinstance(ratio, float)):
            raise ExamException('Ratio non è di tipo intero/float')
        #valore di default pari a 1
        if(ratio == None):
            self.ratio = 1
        else:
            self.ratio = ratio

    def compute(self, lista):

        #eccezione: se un elemento della lista non è di tipo intero o float
        for item in lista:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise ExamException('Un elemento della lista non è di tipo intero o float')
        #eccezione: se la lista è vuota
        if(lista == None):
            raise ExamException('Lista vuota')
        lista_risultato = []
        differenza = 0
        #risultato=rapporto tra differenza e ratio
        risultato = 0
        lunghezza = len(lista)
        i = 0
        #eccezione: se l'indice i è maggiore della lunghezza della lista
        if(i>lunghezza):
            raise ExamException('Indice i maggiore della lunghezza della lista')
        while(i<lunghezza-1):
            differenza = lista[i+1]-lista[i]
            i = i+1
            risultato = differenza/self.ratio
            lista_risultato.append(risultato)
        return lista_risultato

diff = Diff(1)
result_diff = diff.compute([2,4,8,16])
print(result_diff)

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)