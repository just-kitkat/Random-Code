import unittest
import sys
sys.path.append("Caesar Cipher")
from caesar import encrypt, decrypt

class Test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("hello world!!", 1), "ifmmp xpsme!!")
        self.assertEqual(encrypt("hello world!!", 8), "pmttw ewztl!!")
        self.assertEqual(encrypt("hello world!!", 12), "tqxxa iadxp!!")
        self.assertEqual(encrypt("Hello World!!", 12), "tqxxa iadxp!!")
        self.assertEqual(encrypt("Hello World!!", 23), "ebiil tloia!!")
        self.assertEqual(encrypt("Hello World!!", 26), "hello world!!")

    def test_decrypt(self):
        self.assertEqual(decrypt("ifmmp xpsme!!", 1), "hello world!!")
        self.assertEqual(decrypt("pmttw ewztl!!", 8), "hello world!!")
        self.assertEqual(decrypt("tqxxa iadxp!!", 12), "hello world!!")
        self.assertEqual(decrypt("tqxxa iadxp!!", 12), "hello world!!")
        self.assertEqual(decrypt("ebiil tloia!!", 23), "hello world!!")
        self.assertEqual(decrypt("Hello World!!", 26), "hello world!!")
        
if __name__ == "__main__":
    unittest.main()