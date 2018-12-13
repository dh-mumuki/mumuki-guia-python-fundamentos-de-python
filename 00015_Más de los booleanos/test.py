class TestFixtures(unittest.TestCase):
  def un_numero_chico_esiste(self):
    self.assertNotEqual(un_numero_chico, None, 'Recuerda definir la variable un_numero_chico!')
#    
#  def un_numero_chico_esiste(self):
#    self.assertNotEqual(un_numero_grande, None, 'Recuerda definir la variable un_numero_chico!')
#
#  def es_mayor_esiste(self):
#    self.assertNotEqual(es_mayor, None, 'Recuerda definir la variable es_mayor!')
#    
#  def es_menor_esiste(self):
#    self.assertNotEqual(es_menor, None, 'Recuerda definir la variable es_menor!')
#
#  def un_numero_chico_tipo(self):
#    self.assertIs(un_numero_chico, float or int, 'un_numero_chico no parece ser un número!')
#    
#  def un_numero_grande_tipo(self):
#    self.assertIs(un_numero_grande, float or int, 'un_numero_chico no parece ser un número!')
#
#
#  def test_es_mayor(self):
#    self.assertTrue(es_mayor == (un_numero_grande >= un_numero_chico),'un_numero_grande no pareciera ser mayor que un_numero_chico!')
    
#  def test_es_menor(self):
#    self.assertTrue(es_menor == (un_numero_grande <= un_numero_chico),'un_numero_grande no pareciera ser menor que un_numero_chico!')
