#LEZIONE 8
class Model():

    def fit(self, data):
        pass

    def predict(self, data):
        pass

#creo la classe che estente Model
class IncrementModel (Model):

    def __str__(self):
        return 'IncrementModel'

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


#LEZIONE 9
class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):

        #calcolo l'incremento medio su tutto il dataset e non solo sulla predict
        self.global_avg_increment = self.funzione_incremento_medio(fit_data)
        
               
    
    def predict(self, predict_data):
          
        #richiamo la funzione originale
        predict_originale = super().predict(predict_data)

        #sottraggo l'ultimo valore per avere l'incremento prima della presidizione
        incremento_originale = predict_originale - predict_data[-1]

        #incremento medio tra quello del fit(su tutto il dataset) e quello della predict
        media_incrementi = (self.global_avg_increment + incremento_originale)/2

        #sommo la media degli incrementi su tutto il dataset all'ultimo elemento
        prediction = predict_data[-1] + media_incrementi

        return prediction

#tabella
fit_data = [8,19,31,41]
predict_data = [50,52,60]


modello_senza_fit=IncrementModel()
print('Valore ipotetico vendite dicembre: "{}"'.format(modello_senza_fit.predict(predict_data)))

modello_con_fit = FitIncrementModel()
print('modello con fit: "{}"'.format(modello_con_fit.fit(fit_data)))
print('Valore ipotetico vendite dicembre con il modello con fit: "{}"'.format(modello_con_fit.predict(predict_data)))

data = [8,19,31,41,50,52,60]
prediction = 68

from matplotlib import pyplot
pyplot.plot(data + [prediction], color = 'tab:red')
pyplot.plot(data, color = 'tab:blue')
pyplot.show()