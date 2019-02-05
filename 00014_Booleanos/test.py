class TestFixtures(unittest.TestCase):
  def test_valor_de_verdad_existe(self):
    self.assertNotEqual(me_gusta_el_helado, None, msg="¡Acordate de definir la variable!")
  
  def test_valor_de_verdad(self):
    self.assertEqual(me_gusta_el_helado, True)
    