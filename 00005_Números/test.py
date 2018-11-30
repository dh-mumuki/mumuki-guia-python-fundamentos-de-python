class TestFixtures(unittest.TestCase):
   def test_numeros(self):
      self.assertEquals(cinco_float, 5.0)
      
    def test(self):
      self.assertEquals(cinco_integer, 5)

    def test(self):
      self.assertEquals(cinco_string, 'cinco')
      
    def test(self):
      self.assertEquals(verdadero, True)