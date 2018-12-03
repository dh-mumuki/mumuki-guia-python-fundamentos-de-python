estado = "motivados"


class TestFixtures(unittest.TestCase):
   def test_print(self):
      self.assertEquals(mejor_lenguaje_de_programacion, 'Python')
      
   def test_print(self):
      self.assertEquals(mi_nueva_pasion, "Data Science")
      
   def test_print(self):
      self.assertEquals(mi_estado, estado, "ERROR")