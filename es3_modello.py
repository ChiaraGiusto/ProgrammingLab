import numpy as np
import math

data = np.array([[833,37.0], [987,41.6], [883,37.2], [378,15.2], [84,3.4], [483,19.6], [835,35.1], [646,28.9], [508,22.6], [90,3.7]])

#definizione del modello
class LinearModel():
    def __init__(self, angular_coeff=None, intercept=None, train_data=None):
        pass
    
    def fit(self, train_data):
    #controllo che train_data sia della forma giusta
        try:
            assert(len(train_data.shape)==2)
            assert(train_data.shape[1]==2)
        except:
            raise Exception('Bad train_data shape. {} should be (*,2)'. format(train_data.shape))
    #determino il coefficiente angolare (m = self.angular_coeff)
        x = train_data[:,0]
        y = train_data[:,1]
        #media x e y
        mediax = np.mean(x)
        mediay = np.mean(y)
        #coefficiente di correlazione di pearson
        for item in train_data:
            differenzax = train_data[:,0] - mediax
            differenzay = train_data[:,1] - mediay
            numeratore = sum(differenzax*differenzay)
            denominatore = sum((differenzax)**2)*sum((differenzay)**2)
        coeff = numeratore/math.sqrt(denominatore)

        #deviazione standard
        sx = np.std(x,ddof=1)
        sy = np.std(y,ddof=1)
        #coefficie angolare
        self.angular_coeff = coeff * (sy/sx)
    
    #determino il valore dell'intecetta (q = self.intercept)
        self.intercept = mediay + (self.angular_coeff*mediax)

    #?
        self.train_data = train_data
    
    def predict(self, xp):
        #eccezione: caso in cui il coefficiente angolare o l'intecetta non siano stati calcolati
        if(self.angular_coeff == None or self.intercept == None):
            raise Exception('m e/o q non sono stati calcolati')
        y_teorici = []
        i = 0
        for item in xp:
            yi = (self.angular_coeff * xp[i]) + self.intercept
            i = i+1
            y_teorici.append(yi)
        return y_teorici

#applicazione del modello
modello = LinearModel()
fit_modello = modello.fit(data)
prediction = modello.predict([833,987,883,378,84,483,835,646,508,90])
print(fit_modello)
print(prediction)