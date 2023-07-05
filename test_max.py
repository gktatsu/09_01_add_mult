import unittest
from compute import mymax


class TestMymax(unittest.TestCase):

    def test_max(self):
        val = mymax(1, 2)
        self.assertEqual(2, val)

    def test_max_pp(self):
        val = mymax(6, 2)
        self.assertTrue(val > 0)

    def test_max_nn(self):
        val = mymax(-2, -6)
        self.assertTrue(val < 0)

    def test_max_a0(self):
        val = mymax(0, 6)
        self.assertEqual(6, val)

    def test_max_b0(self):
        val = mymax(2, 0)
        self.assertEqual(2, val)
        
    def test_max_n_a0(self):
        val = mymax(0, -3)
        self.assertEqual(0, val)

    def test_max_n_b0(self):
        val = mymax(-2, 0)
        self.assertEqual(0, val)

    def test_max_pn_a_gt_b(self):
        val = mymax(4, -1)
        self.assertTrue(val > 0)

    def test_max_pn_a_lt_b(self):
        val = mymax(1, -4)
        self.assertTrue(val < 0)


if __name__ == "__main__":
    unittest.main()
