import unittest
import src.persistence as persistence


class MyTestCase(unittest.TestCase):
    def test_additive_persistence(self):
        self.assertEqual(persistence.additive_persistence(5), 0)
        self.assertEqual(persistence.additive_persistence(27), 1)
        self.assertEqual(persistence.additive_persistence(58), 2)
        self.assertEqual(persistence.additive_persistence(5789), 3)
        self.assertEqual(persistence.additive_persistence(19999999999999999999999), 4)

    def test_multiplicative_persistence(self):
        self.assertEqual(persistence.multiplicative_persistence(7), 0)
        self.assertEqual(persistence.multiplicative_persistence(1234567890), 1)
        self.assertEqual(persistence.multiplicative_persistence(39), 3)
        self.assertEqual(persistence.multiplicative_persistence(6788), 6)
        self.assertEqual(persistence.multiplicative_persistence(277777788888899), 11)


if __name__ == '__main__':
    unittest.main()
