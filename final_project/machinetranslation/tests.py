import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertRaises(ValueError, english_to_french, None)
        self.assertNotEqual(english_to_french('Hello'), 'Hola')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertRaises(ValueError, french_to_english, None)
        self.assertNotEqual(french_to_english('Bonjour'), 'Hola')

if __name__ == '__main__':
    unittest.main()
