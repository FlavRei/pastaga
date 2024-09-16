import unittest
from pastaga import pastaga

class TestMain(unittest.TestCase):
    def test_pastaga(self):
        compte_les_verres = pastaga(8, 10)
        self.assertEqual(18, compte_les_verres)

    def test_pastaga(self):
        compte_les_verres = pastaga(12, 10)
        self.assertEqual(22, compte_les_verres)

if __name__ == '__main__':
    unittest.main()