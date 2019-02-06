class TestFixtures(unittest.TestCase):
  def un_numero_chico_existe(self):
    self.assertIsNone(un_numero_chico, 'no existe el valor "un_numero_chico"')
    
  def un_numero_chico_esiste(self):
    self.assertIsNone(un_numero_grande)
    
  def es_mayor_esiste(self):
    self.assertIsNone(es_mayor)
    
  def es_menor_esiste(self):
    self.assertIsNone(es_menor)

  def un_numero_chico_tipo(self):
    self.assertTrue(un_numero_chico == float or un_numero_chico == int)
    
  def un_numero_grande_tipo(self):
    self.assertTrue(un_numero_grande == float or un_numero_grande == int)


  def test_es_mayor(self):
    
    self.assertGreater(un_numero_grande, un_numero_chico)
    self.assertTrue(un_numero_grande > un_numero_chico)
    self.assertTrue(es_menor)
    
  def test_es_menor(self):
    self.assertLessEqual(un_numero_chico, un_numero_grande)
    self.assertFalse(es_mayor)
