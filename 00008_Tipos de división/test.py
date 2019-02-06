class TestFixtures(unittest.TestCase):
  def test_maples_cantidad(self):
    self.assertAlmostEqual(maples_completos, 2, "Revisa la cantidad de maples.")
      
  def test_canicas_peso(self):
    self.assertAlmostEqual(peso_cinco_canicas, 84,'El peso de las canicas no es correcto')
    
  