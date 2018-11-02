cinco_float = 5.0
cinco_integer = 5
cinco_string = "cinco"


class TestFixtures(unittest.TestCase):
   def test(self):
      self.assertTrue(cinco_float == 5.0)
      self.assertTrue(cinco_integer == 5)
      self.assertTrue(cinco_string.lower() == "cinco")