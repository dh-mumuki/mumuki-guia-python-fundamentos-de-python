class TestStringMethods(unittest.TestCase):
  def test_string(self):
    self.assertTrue(type(mi_nombre) == str, "Tu nombre debe ser un string")

  def test_integer(self):
    self.assertTrue(type(mi_edad) == int,  "Tu edad debe ser un integer")

    