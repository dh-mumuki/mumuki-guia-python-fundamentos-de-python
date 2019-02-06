class TestFixtures(unittest.TestCase):
  def test_maples_precision(self):
    import sys
    
    self.assertAlmostEqual(maples_completos, 2, sys.version + "La diferencia es significativa.")
      
  def test_canicas_precision(self):
    self.assertAlmostEqual(peso_cinco_canicas, 84,'La diferencia es significatica')