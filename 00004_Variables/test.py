class TestStringMethods(unittest.TestCase):
  def test_String(self):
    self.assertTrue(type(mi_nombre) == str, "¡Tu nombre debe ser un string!")

  def test_Integer(self):
    self.assertTrue(type(mi_edad) == int,  "¡Tu edad debe ser un integer!")

    