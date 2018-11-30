input = '/*...content...*/'
print_test = "print "+"En Pyhton se denomina 'string' a lo que comunmente llamamos 'texto'" 


class TestFixtures(unittest.TestCase):
   def test_print(self):
      self.assertEquals(input, print_test)