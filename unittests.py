import unittest

import netfuncs as nf


class TestNetFunctions(unittest.TestCase):

    def test_ipv4_to_value(self):
        self.assertEqual(nf.ipv4_to_value('255.255.0.0'), 4294901760)
        self.assertEqual(nf.ipv4_to_value('1.2.3.4'), 16909060)

    def test_value_to_ipv4(self):
        self.assertEqual(nf.value_to_ipv4(4294901760), '255.255.0.0')
        self.assertEqual(nf.value_to_ipv4(16909060), '1.2.3.4')


if __name__ == '__main__':
    unittest.main()
