class TestStringMethods(unittest.TestCase):
  def test_string(self):
    
    
    self.assertTrue(isinstance(mi_nombre, (str)), "Tu nombre debe ser un string version" )

  def test_integer(self):
    import types
    NumberTypes = (types.IntType, types.LongType, types.FloatType, types.ComplexType)
    self.assertTrue(isinstance(mi_edad, NumberTypes),  "Tu edad debe ser un integer")

    