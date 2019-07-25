class TestFixtures(unittest.TestCase):
  def test_maples_cantidad(self):
    self.assertAlmostEqual(maples_completos, 2, msg="Revisa la cantidad de maples.")
      
  def test_canicas_peso(self):
    if self.assertAlmostEqual(peso_cinco_canicas, 83.57,msg='El peso de las canicas no es correcto'):
      return True
    elif self.assertAlmostEqual(peso_cinco_canicas, 83.55,msg='El peso de las canicas no es correcto'):
      return True
    else:
      return False