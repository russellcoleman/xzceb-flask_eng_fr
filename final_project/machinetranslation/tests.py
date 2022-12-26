import unittest

from translator import englishToFrench, frenchToEnglish




class TestClass (unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual( 'bonjour' ,englishToFrench( 'hello'))
    def test_french_to_english (self):
        self.assertEqual( 'hello', frenchToEnglish('bonjour'))
