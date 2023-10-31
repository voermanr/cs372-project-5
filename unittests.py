import unittest

import netfuncs as nf
import json


class TestNetFunctions(unittest.TestCase):

    def test_ipv4_to_value(self):
        self.assertEqual(nf.ipv4_to_value('255.255.0.0'), 4294901760)
        self.assertEqual(nf.ipv4_to_value('1.2.3.4'), 16909060)

    def test_value_to_ipv4(self):
        self.assertEqual(nf.value_to_ipv4(4294901760), '255.255.0.0')
        self.assertEqual(nf.value_to_ipv4(16909060), '1.2.3.4')

    def test_subnet_mask_value(self):
        self.assertEqual(nf.get_subnet_mask_value('/16'), 4294901760)
        self.assertEqual(nf.get_subnet_mask_value('10.20.30.40/23'), 4294966784)

    def test_ips_same_subnet(self):
        self.assertTrue(nf.ips_same_subnet(
            ip1="10.23.121.17",
            ip2="10.23.121.225",
            slash="/23"
        ))

        self.assertFalse(nf.ips_same_subnet(
            ip1="10.23.230.22",
            ip2="10.24.121.225",
            slash="/16"
        ))

    def get_network(self):
        self.assertEqual(nf.get_network(0x01020304, 0xffffff00), 0x01020300)

    def find_router_for_ip(self):
        routers = json.loads('{ "1.2.3.1": { "netmask": "/24"},"1.2.4.1": {"netmask": "/24"}}')

        self.assertEqual(nf.find_router_for_ip(routers=routers, ip="1.2.3.5"), "1.2.3.1")
        self.assertEqual(nf.find_router_for_ip(routers=routers, ip="1.2.5.6"), None)

if __name__ == '__main__':
    unittest.main()
