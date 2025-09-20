import unittest
from extraterrestres import guardar_string_matriz

class TestGuardarMatrizStrings(unittest.TestCase):

    def test_verificar_traza_todo_true(self):
        matrix = guardar_string_matriz("holamundo")
        for i in range(len(matrix)):
            self.assertEqual(matrix[i][i], True)

if __name__ == "__main__":
    unittest.main()