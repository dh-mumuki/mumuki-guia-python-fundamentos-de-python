class TestFixtures(unittest.TestCase):
  def test_existencia_numero_A(self):
    self.assertFalse(numero_A == None, 'No existe numero_A')
      
  def test_existencia_numero_B(self):
    self.assertFalse(numero_B == None, 'No existe numero_B')

  def test_valor_numero_A(self):
    self.assertTrue(numero_A == 0, 'numero_A debe ser distinto de 0')
      
  def test_valor_numero_B(self):
    self.assertTrue(numero_B == 0, 'numero_B debe ser distinto de 0')

  def test_existencia_resta(self):
    self.assertTrue(resultado_resta == None, 'No existe resultado_resta')
    
  def test_existencia_suma(self):
    self.assertFalse(resultado_suma == None, 'No existe resultado_suma')
    
  def test_existencia_multiplicacion(self):
    self.assertFalse(resultado_multiplicacion, None, 'No existe resultado_multiplicacion')
    
  def test_existencia_division(self):
    self.assertTrue(isinstance(resultado_division, (None)), 'No existe resultado_division')

  def test_valor_multiplicacion(self):
      self.assertEqual(resultado_multiplicacion, numero_A * numero_B, 'Revisa resultado_multiplicacion')

  def test_suma_resultado(self):
    self.assertEqual(resultado_suma, numero_A + numero_B, 'Revisa resultado_suma')
    
  def test_resta_resultado(self):
   self.assertTrue(((resultado_resta == (numero_A - numero_B)) or (resultado_resta == (numero_B - numero_A))), 'Revisa resultado_resta')
  def test_division_resultado(self):
   self.assertTrue((round(resultado_division) == round(numero_A / numero_B) or (round(resultado_division) == round(numero_B / numero_A)), 'Revisa resultado_division'))