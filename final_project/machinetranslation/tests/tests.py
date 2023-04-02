import unittest
from translator import englishToFrench, frenchToEnglish

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test When the string ‘Bonjour’ is given as input the output must be ‘Hello’.
        self.assertEqual(frenchToEnglish(None), "null input") # test When the string is None

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test When the string ‘Hello’ is given as input the output must be ‘Bonjour’.
        self.assertEqual(englishToFrench(None), "null input") # test When the string is None

unittest.main()