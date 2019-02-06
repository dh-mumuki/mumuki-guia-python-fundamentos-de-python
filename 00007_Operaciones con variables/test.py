class TestFixtures(unittest.TestCase):
  def test_numero_A(self):
    self.assertNotEqual(numero_A, None, '¡No existe numero_A!')
      
  def test_numero_B_existencia(self):
    self.assertNotEqual(numero_B, None, '¡No existe numero_B!')

  def test_numero_A_cero(self):
    self.assertNotEqual(numero_A, 0, '¡numero_A debe ser distinto de 0!')
      
  def test_numero_B_cero(self):
    self.assertNotEqual(numero_B, 0, '¡numero_B debe ser distinto de 0!')

  def test_resultado_resta_existencia(self):
    self.assertNotEqual(resultado_resta, None, '¡No existe resultado_resta!')
    
  def test_resultado_suma_existencia(self):
    self.assertNotEqual(resultado_suma, None, '¡No existe resultado_suma!')
    
  def test_resultado_multiplicacion_existencia(self):
    self.assertNotEqual(resultado_multiplicacion, None, '¡No existe resultado_multiplicacion!')

  def test_resultado_division_existencia(self):
    self.assertNotEqual(resultado_division, None, '¡No existe resultado_division!')

  def test_resultado_multiplicacion(self):
      self.assertEqual(resultado_multiplicacion, numero_A * numero_B, '¡Revisá resultado_multiplicacion!')

  def test_resultado_suma(self):
    self.assertEqual(resultado_suma, numero_A + numero_B, '¡Revisá resultado_suma!')
    
  def test_resultado_resta1(self):
   self.assertTrue(((resultado_resta == (numero_A - numero_B)) or (resultado_resta == (numero_B - numero_A))), '¡Revisa resultado_resta!')
  def test_resultado_division1(self):
   self.assertTrue((round(resultado_division) == round(numero_A / numero_B) or (round(resultado_division) == round(numero_B / numero_A)), '¡Revisa resultado_division!'))