import unittest
from calculadora import soma, subtrai

class TesCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5),10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5),0)

    def test_soma_varias_entradas(self):
        x_y_saidas =(
            (10,10,20),
            (10,20,30),
            (10,5,15),
            (-10,10,0),
            (3.3,3.3,6.6),
            (-3,-2,-5),
            (6,6,12),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x , y , saida = x_y_saida
                self.assertEqual(soma(x,y),saida)

    def test_soma_x_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma('11',0)

    def test_soma_y_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma(11,'0')

    
    def test_subtrai_5_e_5_deve_retornar_0(self):
            self.assertEqual(subtrai(5,5),0)
    
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(-5,5),-10)

    def test_subtrai_varias_entradas(self):
        x_y_saidas =(
            (10,10,0),
            (10,20,-10),
            (10,5,5),
            (-10,10,-20),
            (3.3,3.3,0),
            (-3,-2,-1),
            (6,6,0),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x , y , saida = x_y_saida
                self.assertEqual(subtrai(x,y),saida)


    def test_soma_x_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            subtrai('11',0)

    def test_soma_y_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            subtrai(11,'0')



if __name__ == '__main__':
    unittest.main(verbosity=2)