class TestFixtures(unittest.TestCase):
  def un_numero_chico_esiste(self):
    self.assertNotEqual(un_numero_chico, None, 'Recuerda definir la variable un_numero_chico!')
    
#  def un_numero_chico_esiste(self):
#    self.assertNotEqual(un_numero_grande, None, 'Recuerda definir la variable un_numero_chico!')


#  def es_mayor_esiste(self):
#    self.assertNotEqual(es_mayor, None, 'Recuerda definir la variable es_mayor!')
    
#  def es_mayor_esiste(self):
#    self.assertNotEqual(es_menor, None, 'Recuerda definir la variable es_mayor!')

#  def un_numero_chico_esiste(self):
#    self.assertIs(un_numero_chico, float or int, 'Recuerda definir la variable un_numero_chico!')
    
#  def un_numero_chico_esiste(self):
#    self.assertIs(un_numero_grande, float or int, 'Recuerda definir la variable un_numero_chico!')

#  def un_numero_chico_esiste(self):
#    self.assertIs(es_mayor, float or int, 'Recuerda definir la variable un_numero_chico!')
    
#  def un_numero_chico_esiste(self):
#    self.assertTrue(es_mayor == un_numero_grande >= un_numero_chico,'Recuerda definir la variable un_numero_chico!')
    
#  def un_numero_chico_esiste(self):
    self.assertTrue(es_menor == un_numero_grande <= un_numero_chico,'Recuerda definir la variable un_numero_chico!')
