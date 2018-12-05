class TestFixtures(unittest.TestCase):
  def test(self):
    self.assertIsNotNone(mi_nombre)
    
  def test(self):
    self.assertTrue(type(mi_nombre) == str, "Debe ser un string!")
  
  def test(self):
    self.assertIsNotNone(mi_edad)
  
  def test(self):
    self.assertEqual(type(mi_edad), int,  "Debe ser un integer!")