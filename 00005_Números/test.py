class TestFixtures(unittest.TestCase):
  def test_numeros(self):
    self.assertEquals(cinco_float, 5.0)

  def test_numeros(self):
    self.assertTrue(type(cinco_float) == float)
      
  def test(self):
    self.assertEquals(cinco_integer, 5)

  def test(self):
    self.assertEquals(cinco_string, 'cinco')