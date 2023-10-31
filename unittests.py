import unittest

from netfuncs import ipv4_to_value


class TestNetFunctions(unittest.TestCase):

    def test_ipv4_to_value(self):
        self.assertEqual(ipv4_to_value('255.255.0.0'), 4294901760)
        self.assertEqual(ipv4_to_value('1.2.3.4'), 16909060)


if __name__ == '__main__':
    unittest.main()
