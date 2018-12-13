class TestFixtures(unittest.TestCase):
  def un_numero_chico_esiste(self):
    self.assertNotEqual(un_numero_chico, None, 'Recuerda definir la variable un_numero_chico!')
