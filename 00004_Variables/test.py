class TestStringMethods(unittest.TestCase):
  def test_string(self):
    
    self.assertTrue(isinstance(mi_nombre, (str)), "Tu nombre debe ser un string version" )

  def test_integer(self):
    self.assertTrue(isinstance(mi_edad, (int)),  "Tu edad debe ser un integer")

    