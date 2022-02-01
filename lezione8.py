#creo la super classe
class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

#creo la classe che estente Model
class IncrementModel (Model):

    def funzione_incremento_medio(self, data):
        
        #variabile di supporto per il valore precedente
        precedente = None

        #variabile di supposto per calcolare l'incremento 
        incremento = 0

        for item in data:
            #calcolo l'incremento ma non al primo giro dove "precendente" non è definito
            if precedente is not None:
                incremento = incremento + (item - precedente)
            precedente = item
        
        #calcolo l'incremento medio
        incremento_medio = incremento/(len(data)-1)
        return incremento_medio
    
    def predict(self, predict_data):

        #calcolo l'incremento medio sui dati della predict
        incremento_medio_predict = self.funzione_incremento_medio(predict_data)

        #torno la prediction (incremento medio sommato all'ultimo valore)
        prediction = predict_data[-1] + incremento_medio_predict
        
        return prediction

#tabella
dicembre=IncrementModel()
print('Valore ipotetico vendite dicembre: "{}"'.format(dicembre.predict([50, 52, 60])))