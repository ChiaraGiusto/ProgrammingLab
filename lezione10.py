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


#LEZIONE 10
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# mesi usare per la valutazione che verranno sottratti al dataset nel caso del fit
mesi_val = 12
mesi_fit = len(shampoo_sales) - mesi_val #24

# Istanzio modello senza fit
modello_senza_fit = IncrementModel()

# Istanzio modello con fit
modello_con_fit = FitIncrementModel()

modello_con_fit.fit(shampoo_sales[0:mesi_fit])

# Metto entrambi i modelli in una lista
modelli = [modello_senza_fit, modello_con_fit]

# Swicth per il plot (se messo a True bisogna chiudere la finestra del plot per far proseguire il programma dopo la valutazione del primo modello)
plot = False

# Valuto entrambi i modelli
for modello in modelli:

    errore = 0
    print('Valutazione modelli "{}"'.format(modello))

    # Predizioni sul dataset di "valutazione" ovvero le vendite dello shampoo dal 24esimo mese in poi
    predictions = []
    for i in range(mesi_val):

        predict_data = shampoo_sales[mesi_fit+i-3-1:mesi_fit+i-1]
        prediction = modello.predict(predict_data)
        real = shampoo_sales[mesi_fit+i]
        print('"{}" (prediction) vs "{}" (real)'.format(int(prediction), int(real)))

        # Aggiungo se volessi poi plottare
        predictions.append(prediction)

        errore += abs(prediction - shampoo_sales[mesi_fit+i])
    
    #calcolo l'errore medio
    errore = errore / mesi_val

    print('Errore medio: "{}"\n'.format(errore))

    if plot:
        from matplotlib import pyplot
        pyplot.plot(shampoo_sales[0:mesi_fit] + predictions, color = 'tab:red')
        pyplot.plot(shampoo_sales, color = 'tab:blue')
        pyplot.show()