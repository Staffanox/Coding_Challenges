import unittest

import switch_on_gravity as sog


class MyTestCase(unittest.TestCase):
    def test_first_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["-", "#", "#", "-"],
            ["-", "-", "#", "-"],
            ["-", "-", "-", "-"],
        ]), [
            ["-", "-", "-", "-"],
            ["-", "-", "#", "-"],
            ["-", "#", "#", "-"]
        ])

    def test_second_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["-", "#", "#", "-"],
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"]
        ]), [
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
            ["-", "#", "#", "-"]
        ])

    def test_third_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["-", "#", "#", "#", "#", "-"],
            ["#", "-", "-", "#", "#", "-"],
            ["-", "#", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"]
        ]), [
            ["-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["-", "#", "-", "#", "#", "-"],
            ["#", "#", "#", "#", "#", "-"]
        ])

    def test_fourth_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["-", "#", "#", "#", "#", "-"],
            ["#", "-", "-", "#", "#", "-"],
            ["-", "#", "-", "-", "-", "-"],
            ["-", "#", "-", "#", "-", "-"]
        ]), [
            ["-", "-", "-", "-", "-", "-"],
            ["-", "#", "-", "#", "-", "-"],
            ["-", "#", "-", "#", "#", "-"],
            ["#", "#", "#", "#", "#", "-"]
        ])

    def test_fifth_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["-", "#", "#", "-"],
            ["-", "-", "#", "-"],
            ["#", "#", "-", "-"],
        ]), [
            ["-", "-", "-", "-"],
            ["-", "#", "#", "-"],
            ["#", "#", "#", "-"]
        ])

    def test_sixth_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["#"],
            ["-"],
            ["#"],
            ["-"]
        ]), [
            ["-"],
            ["-"],
            ["#"],
            ["#"]
        ])

    def test_seventh_gravity(self):
        self.assertEqual(sog.switch_gravity_on([
            ["#"],
            ["#"],
            ["#"],
            ["#"]
        ]), [
            ["#"],
            ["#"],
            ["#"],
            ["#"]
        ])


if __name__ == '__main__':
    unittest.main()
