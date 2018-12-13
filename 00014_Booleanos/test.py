class TestFixtures(unittest.TestCase):
  def test_valor_de_verdad_esiste(self):
    self.assertFalse(me_gusta_el_helado, None, 'Recuerda definir la variable me_gusta_el_helado')
    
  def test_valor_de_verdad(self):
    self.assertTrue(me_gusta_el_helado, "Revisa la variable me_gusta_el_helado, no parece ser igual a True")