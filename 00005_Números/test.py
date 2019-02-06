class TestFixtures(unittest.TestCase):
  def test_numeros_float(self):
    self.assertTrue(isinstance(cinco_float, (float)), 'La coma en los tipo de datos floats, es un punto.')
    self.assertTrue(cinco_float == 5, 'El valor es incorrecto')
  

  def test_numero_integer(self):
    self.assertTrue(cinco_integer == 5, 'Este numero {}, no tiene el valor requerido. '.format( cinco_integer))
    self.assertTrue(isinstance(cinco_integer, (int)), 'Este numero {}, no es un entero '.format( cinco_integer)) 
  
  def test_numero_string(self):
    self.assertTrue(isinstance(cinco_string, (str)), 'El tipo de datos no es correcto (no es str).')
    self.assertTrue((cinco_string == '5') | (cinco_string.lower() == 'cinco'), 'No se corresponde con la magnitud 5')