class TestFixtures(unittest.TestCase):
  def test_valor_de_verdad_esiste(self):
    self.assertNotEqual(me_gusta_el_helado, None)
    
  def test_valor_de_verdad(self):
    self.assertTrue(me_gusta_el_helado == True)