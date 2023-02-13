import unittest
from resist import resist

class TestResist(unittest.TestCase):
    def test_resist(self):
        self.assertAlmostEqual(resist("(10, [20, 30])"), 22.0, places=1)
        self.assertAlmostEqual(resist("[10, (20, 30)]"), 8.3, places=1)
        self.assertAlmostEqual(resist("([10, 20], (30, 40))"), 76.7, places=1)
        self.assertAlmostEqual(resist("(1, [12, 4, (1, [10, (2, 8)])])"), 3.0, places=1)
        self.assertAlmostEqual(resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"), 10.0, places=1)

if __name__ == '__main__':
    unittest.main()
