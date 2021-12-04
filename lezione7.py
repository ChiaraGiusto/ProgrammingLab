import unittest
from lezione5_parte1 import __init__ #verifico che il nome del file sia salvato come attributo

#creo una classe che estende TestCase
class Test_attributo(unittest.TestCase):

    def test_attributo(self):
        self.assertEqual(__init__(name), self.name)
        
        #if not __init__(name) == self.name:
            #raise Exception ('Test attributo non passato')