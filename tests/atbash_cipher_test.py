import unittest
import src.atbash_cipher as ab


class MyTestCase(unittest.TestCase):
    def test_all_lowercase(self):
        self.assertEqual(ab.atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")

    def test_all_uppercase(self):
        self.assertEqual(ab.atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")

    def test_sentence(self):
        self.assertEqual(
            ab.atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."),
            "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")

    def test_second_sentence(self):
        self.assertEqual(ab.atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),
                         "Encryption and decryption are identical for the Atbash cipher.")


if __name__ == '__main__':
    unittest.main()


