import unittest
from escenario import verificar_centro, espejar_escenario_sin_centro, espejar_escenario_y_centro, formar_escenario

class TestVerificarCentro(unittest.TestCase):
    
    "--- TESTS PARA VERIFICAR CENTROS ---"

    def test_sin_valor_impar(self):
        arr = [1,1,2,2,3,3]
        self.assertEqual(verificar_centro(arr), 0)

    def test_un_valor_impar(self):
        arr = [1,1,2,2,3]
        self.assertEqual(verificar_centro(arr), 3)

    def test_mas_de_un_valor_impar(self):
        arr = [1,2,2,3]
        self.assertEqual(verificar_centro(arr), -1)

    def test_array_vacio(self):
        arr = []
        self.assertEqual(verificar_centro(arr), 0)

    def test_un_solo_elemento(self):
        arr = [7]
        self.assertEqual(verificar_centro(arr), 7)

class TestEspejosSinCentro(unittest.TestCase):
    
    "--- TESTS PARA VERIFICAR ESPEJOS SIN CENTRO ---"

    def test_array_simple(self):
        self.assertEqual(
            espejar_escenario_sin_centro([5,5,6,6,7,7]),
            [7,6,5,5,6,7]
        )

    def test_array_mas_largo(self):
        self.assertEqual(
            espejar_escenario_sin_centro([1,1,2,2,3,3,4,4]),
            [4,3,2,1,1,2,3,4]
        )

    def test_array_minimo(self):
        self.assertEqual(
            espejar_escenario_sin_centro([9,9]),
            [9,9]
        )

    def test_array_con_valores_grandes(self):
        self.assertEqual(
            espejar_escenario_sin_centro([10,10,20,20,30,30,40,40]),
            [40,30,20,10,10,20,30,40]
        )

    def test_array_con_valores_iguales(self):
        self.assertEqual(
            espejar_escenario_sin_centro([5,5,5,5,5,5,5,5,7,7]),
            [7,5,5,5,5,5,5,5,5,7]
        )

class TestEspejosConCentro(unittest.TestCase):
    
    "--- TESTS PARA VERIFICAR ESPEJOS CON CENTRO ---"

    def test_array_simple_y_centro(self):
        self.assertEqual(
            espejar_escenario_y_centro([1,2,2,3,3,4,4], 1),
            [4,3,2,1,2,3,4]
        )
    
    def test_array_minimo_y_centro(self):
        self.assertEqual(
            espejar_escenario_y_centro([9], 9),
            [9]
        )

    def test_array_con_centro_igual(self):
        self.assertEqual(
            espejar_escenario_y_centro([1,1,2,2,3,3,3], 3),
            [3,2,1,3,1,2,3]
        )

    def test_array_con_valores_grandes_y_centro(self):
        self.assertEqual(
            espejar_escenario_y_centro([10,10,10,20,20,30,30], 10),
            [30,20,10,10,10,20,30]
        )

    def test_array_con_valores_iguales_y_centro(self):
        self.assertEqual(
            espejar_escenario_y_centro([5,5,5,5,5,5,5,5,5,7,7], 5),
            [7,5,5,5,5,5,5,5,5,5,7]
        )
    
class TestFormarEscenario(unittest.TestCase):
    "--- TEST FORMAR ESCENARIOS ---"

    def test_formar_un_escenario_sin_centro(self):
        self.assertEqual(
            formar_escenario([5,2,5,3,1,3,1,2,7,7]),
            [7,5,3,2,1,1,2,3,5,7]
        )
    
    def test_formar_un_escenario_con_centro(self):
        self.assertEqual(
            formar_escenario([5,2,6,2,4,4,6,8,8]),
            [8,6,4,2,5,2,4,6,8]
        )

    def test_formar_un_escenario_invalido(self):
        self.assertEqual(
            formar_escenario([5,1]),
            [-1]
        )
    
    def test_formar_un_escenario_con_valores_iguales_sin_centro(self):
        self.assertEqual(
            formar_escenario([7,5,5,5,5,5,5,5,5,7,9,9]),
            [9,7,5,5,5,5,5,5,5,5,7,9]
        )
    
    def test_formar_un_escenario_con_valores_iguales(self):
        self.assertEqual(
            formar_escenario([7,5,5,5,5,5,5,5,5,5,5]),
            [5,5,5,5,5,7,5,5,5,5,5]
        )


if __name__ == "__main__":
    unittest.main()