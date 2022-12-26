import unittest

from translator import englishToFrench, frenchToEnglish




class TestClass (unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual( englishToFrench( 'hello'), 'Bonjour')
    def test_frenchToEnglish (self):
        self.assertEqual( frenchToEnglish( 'bonjour'), 'Hello')
    def test_englishToFrench2(self):
        self.assertNotEqual( englishToFrench( 'hello'), 'Salut')
    def test_frenchToEnglish2 (self):
        self.assertNotEqual( frenchToEnglish( 'salut'), 'Hello')


unittest.main()

