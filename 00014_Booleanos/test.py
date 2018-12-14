class TestFixtures(unittest.TestCase):
  def test_valor_de_verdad_esiste(self):
    self.assertNotEqual(me_gusta_el_helado, None)
    
  def test_valor_de_verdad_esiste(self):
    try:
      self.assertNotEqual(me_gusta_el_helado, 1, "Intenta con un valor distino de 1")    
    except Exception as e:
      print e
      raise Exception
      
  def test_valor_de_verdad(self):
    self.assertEqual(me_gusta_el_helado, True)
    