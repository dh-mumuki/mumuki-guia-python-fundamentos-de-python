class TestFixtures(unittest.TestCase):
  
  def un_numero_chico_existe(self):
    self.assertTrue('un_numero_chico' in globals(), 'no existe el valor un_numero_chico')
    
  def un_numero_grande_existe(self):
    self.assertTrue('un_numero_grande' in globals(), 'no existe el valor un_numero_grande')
    
  def es_mayor_existe(self):
    self.assertTrue('es_mayor' in globals(), 'no existe el valor es_mayor')
    
  def es_menor_existe(self):
    self.assertTrue('es_menor' in globals(), 'no existe el valor es_menor')
  
  def un_numero_chico_tipo(self):
    self.assertTrue(un_numero_chico == float or un_numero_chico == int, 'La variable un_numero_chico no es un numero')
    
  def un_numero_grande_tipo(self):
    self.assertTrue(un_numero_grande == float or un_numero_grande == int, 'La variable un_numero_grande no es un numero')


  def test_es_mayor(self):
    
    self.assertGreater(un_numero_grande, un_numero_chico, 'un_numero_grande no es mayor a un_numero_chico')
    
    
  def test_es_menor(self):
    self.assertLessEqual(un_numero_chico, un_numero_grande, 'un_numero_chico no es menor o igual a un_numero_grande')
    self.assertFalse(es_mayor)
