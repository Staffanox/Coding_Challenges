import unittest
import src.concert_seats as cs


class MyTestCase(unittest.TestCase):

    def test_first_positive(self):
        self.assertTrue(cs.can_see_stage([[1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9]]), True)

    def test_second_positive(self):
        self.assertTrue(cs.can_see_stage([[1, 1, 2],
                                          [5, 2, 3],
                                          [6, 4, 4]]), True)

    def test_third_positive(self):
        self.assertTrue(cs.can_see_stage([[0, 0, 0],
                                          [1, 1, 1],
                                          [2, 2, 2]]), True)

    def test_last_positive(self):
        self.assertTrue(cs.can_see_stage([[1, 2, 3, 2, 1, 1],
                                          [2, 4, 4, 3, 2, 2],
                                          [5, 5, 5, 5, 4, 4],
                                          [6, 6, 7, 6, 5, 5]]), True)

    def test_first_negative(self):
        self.assertFalse(cs.can_see_stage([[1, 2, 2],
                                           [1, 2, 3],
                                           [4, 4, 4]]), False)

    def test_second_negative(self):
        self.assertFalse(cs.can_see_stage([[1, 1, 2],
                                           [5, 2, 3],
                                           [4, 4, 4]]), False)

    def test_third_negative(self):
        self.assertFalse(cs.can_see_stage([[2, 0, 0],
                                           [1, 1, 1],
                                           [2, 2, 2]]), False)

    def test_fourth_negative(self):
        self.assertFalse(cs.can_see_stage([[1, 0, 0],
                                           [1, 1, 1],
                                           [2, 2, 2]]), False)

    def test_last_negative(self):
        self.assertFalse(cs.can_see_stage([[1, 2, 3, 2, 1, 1],
                                           [2, 4, 4, 3, 2, 2],
                                           [5, 5, 5, 10, 4, 4],
                                           [6, 6, 7, 6, 5, 5]]), False)


if __name__ == '__main__':
    unittest.main()
