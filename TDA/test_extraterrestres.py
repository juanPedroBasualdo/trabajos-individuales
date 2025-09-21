import unittest
from extraterrestres import palindromo_mas_largo

class TestSubstringPalindromoMasLargo(unittest.TestCase):
    
    def test_devuelve_palindromo_correcto(self):
        self.assertEqual(
            palindromo_mas_largo("BANANAS"),
            "ANANA"
        )
    
    def test_devuelve_primera_letra_sin_palindromo(self):
        self.assertEqual(
            palindromo_mas_largo("AVENTURA"),
            "A"
        )
        
    def test_muchos_palindromos_devuelve_primero(self):
        self.assertEqual(
            palindromo_mas_largo("neuquenabcniuquin"),
            "neuquen"
        )
    
    def test_palindromo_larguisimo(self):
        self.assertEqual(
            palindromo_mas_largo("amanaplanacanalpanama"),
            "amanaplanacanalpanama"
        )
    
    def test_palindromo_de_dos_letras(self):
        self.assertEqual(
            palindromo_mas_largo("AABBCC"),
            "CC"
        )

if __name__ == "__main__":
    unittest.main()