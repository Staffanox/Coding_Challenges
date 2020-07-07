import unittest
import src.josephus_permutation as jp


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(jp.who_goes_free(9, 2), 2)

    def test_second(self):
        self.assertEqual(jp.who_goes_free(7, 2), 6)

    def test_third(self):
        self.assertEqual(jp.who_goes_free(9, 3), 0)

    def test_fourth(self):
        self.assertEqual(jp.who_goes_free(7, 3), 3)

    def test_fifth(self):
        self.assertEqual(jp.who_goes_free(15, 4), 12)

    def test_sixth(self):
        self.assertEqual(jp.who_goes_free(14, 3), 1)

    def test_seventh(self):
        self.assertEqual(jp.who_goes_free(53, 7), 21)

    def test_eighth(self):
        self.assertEqual(jp.who_goes_free(543, 21), 455)

    def test_ninth(self):
        self.assertEqual(jp.who_goes_free(673, 13), 303)


if __name__ == '__main__':
    unittest.main()
