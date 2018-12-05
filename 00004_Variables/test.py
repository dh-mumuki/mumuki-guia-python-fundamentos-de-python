class TestFixtures(unittest.TestCase):
  def test(self):
    self.assertIs(mi_nombre,str, "Debe ser un string!")

  def test(self):
    self.assertTrue(type(mi_edad) == int,  "Debe ser un integer!")