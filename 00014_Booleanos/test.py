class TestFixtures(unittest.TestCase):
  def test_helado_existencia(self):
    self.assertTrue('me_gusta_el_helado' in globals(), msg="Acordate de definir la variable")
  
  def test_valor_de_verdad(self):
    self.assertTrue(isinstance(me_gusta_el_helado, (bool)), 'El valor no es un booleano ("True o False")')
    self.assertEqual(me_gusta_el_helado, True, 'El valor de verdad no es correcto')
    