class TestFixtures(unittest.TestCase):
  def test_maples_precision(self):
    import sys
    print(sys.version)
    self.assertAlmostEqual(maples_completos, 2, "La diferencia es significativa.")
      
  def test_canicas_precision(self):
    self.assertAlmostEqual(peso_cinco_canicas, 84,'La diferencia es significatica')