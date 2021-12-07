#creo la super classe
class Model():

    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

#creo la classe che estente Model
class IncrementModel (Model):

    def predict(self, data):
        
        differenza=0
        for n in data:
            differenza = (data[-2]-data[-3])#52-50
            differenza = differenza + (data[-1]-data[-2])#2+(60-52)

        prediction = data[-1] + (differenza/2)#60+5
        return prediction

#tabella
dicembre=IncrementModel()

dicembre.predict(data=[50, 52, 60])
print('Valore ipotetico vendite dicembre: "{}"'.format(dicembre.predict([50, 52, 60])))