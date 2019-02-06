class TestFixtures(unittest.TestCase):
  def test_numeros_float(self):
    self.assertTrue(isinstance(cinco_float, (float)) and cinco_float == 5, 'La coma en los tipo de datos floats, es un punto.')

  def test_numero_integer(self):
    self.assertTrue(cinco_integer == 5 and isinstance(cinco_integer, (int)), 'Este numero %s, no es un entero o no tiene el valor requerido'.format( cinco_integer)) 
  
  def test_numero_string(self):
    self.assertTrue((cinco_string == '5') | (cinco_string.lower() == 'cinco'))