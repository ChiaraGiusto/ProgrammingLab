import unittest
from lezione5_parte1 import CSVFile 

#creo una classe che estende TestCase
class TestAttributo(unittest.TestCase):

    def test_nome(self):
        file = CSVFile('Vendite shampoo', 'sales_lezione3.csv')

        #verifico che il nome del file sia salvato come attributo
        self.assertEqual(file.name, 'sales_lezione3.csv')
        
        if not file.name == 'sales_lezione3.csv':
            raise Exception ('Test attributo non passato')

unittest.main()