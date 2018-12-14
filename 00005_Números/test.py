class TestFixtures(unittest.TestCase):
  def test_numeros_float(self):
    self.assertEquals(cinco_float, 5.0)

  def test_numeros_float_tipo(self):
    self.assertTrue(type(cinco_float) == float)
      
  def test_numero_integer_valor(self):
    self.assertEquals(cinco_integer, 5)
  
  def test_numeros_integer_tipo(self):
    self.assertTrue(type(cinco_integer) == int )

  def test_numero_string(self):
    self.assertEquals(cinco_string, 'cinco')