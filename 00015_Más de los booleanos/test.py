class TestFixtures(unittest.TestCase):
  def un_numero_chico_existe(self):
    self.assertTrue("un_numero_chico" in globals())
    
  def un_numero_chico_esiste(self):
    
    self.assertNotEqual("un_numero_grande" in globals())
    
    raise Except:
      print(globals())

  def es_mayor_esiste(self):
    self.assertNotEqual(es_mayor, None)
    
  def es_menor_esiste(self):
    self.assertNotEqual(es_menor, None)

  def un_numero_chico_tipo(self):
    self.assertTrue(un_numero_chico == float or un_numero_chico == int)
    
  def un_numero_grande_tipo(self):
    self.assertTrue(un_numero_grande == float or un_numero_grande == int)


  def test_es_mayor(self):
    self.assertTrue(es_mayor == (un_numero_grande >= un_numero_chico))
    
  def test_es_menor(self):
    self.assertTrue(es_menor == (un_numero_chico <= un_numero_grande))