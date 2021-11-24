class CSVFile ():
    # inizializzo l'oggetto e aggiungo l'attributo
    def __init__ (self, file, name):
        self.file = file
        self.name = name
    
    #metodo get_data
    def get_data(self):
        my_list=[]
        my_file = open('sales_lezione3.csv', 'r')
        for line in my_file:
            elem = line.split(',')
            if elem[0] != 'Date':
                my_list.append(elem)
        my_file.close()
        return my_list

mia_lista = []
obj = CSVFile('Vendite shampoo', 'sales_lezione3.csv')
mia_lista = obj.get_data()
print ('Nome file: {}'.format(obj.name))
print('Contenuto: ')
for x in mia_lista:
    #print("['{}, {}']".format(x[0], x[1]))
    print(x)

        

