class TestFixtures(unittest.TestCase):
  def test_numero_A(self):
    self.assertNotEqual(numero_A, None, 'No existe numero_A!')
      
  def test_numero_B_existencia(self):
    self.assertNotEqual(numero_B, None, 'No existe numero_B!')

  def test_resultado_resta_existencia(self):
    self.assertNotEqual(resultado_resta, None, 'No existe resultado_resta!')
    
  def test_resultado_suma_existencia(self):
    self.assertNotEqual(resultado_suma, None, 'No existe resultado_suma!')
    
  def test_resultado_multiplicacion_existencia(self):
    self.assertNotEqual(resultado_multiplicacion, None, 'No existe resultado_multiplicacion!')

  def test_resultado_division_existencia(self):
    self.assertNotEqual(resultado_division, None, 'No existe resultado_division!')

  def test_resultado_division(self):
    self.assertAlmostEqual(resultado_division, numero_A / numero_B, 'Revisa resultado_division!')

  def test_resultado_multiplicacion(self):
      self.assertEqual(resultado_multiplicacion, numero_A * numero_B, 'Revisa resultado_multiplicacion!')

  def test_resultado_suma(self):
    self.assertEqual(resultado_suma, numero_A + numero_B, 'Revisa resultado_suma!')
    
  def test_resultado_resta1(self):
   self.assertTrue(((resultado_resta == (numero_A - numero_B)) or (resultado_resta == (numero_B - numero_A))), True)

  def test_resultado_division1(self):
   self.assertTrue(((round(resultado_division,5) == round((numero_A / numero_B)),5) or (round(resultado_resta,5) == round((numero_B - numero_A)),5), True)
