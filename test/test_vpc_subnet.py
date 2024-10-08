# coding: utf-8

"""
    Oxide Region API

    API for interacting with the Oxide control plane

    The version of the OpenAPI document: 20240821.0
    Contact: api@oxide.computer
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from oxide.models.vpc_subnet import VpcSubnet

class TestVpcSubnet(unittest.TestCase):
    """VpcSubnet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VpcSubnet:
        """Test VpcSubnet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VpcSubnet`
        """
        model = VpcSubnet()
        if include_optional:
            return VpcSubnet(
                custom_router_id = '',
                description = '',
                id = '',
                ipv4_block = '192.168.1.0/24',
                ipv6_block = 'fd12:3456::/64',
                name = ERROR_TO_EXAMPLE_VALUE,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                vpc_id = ''
            )
        else:
            return VpcSubnet(
                description = '',
                id = '',
                ipv4_block = '192.168.1.0/24',
                ipv6_block = 'fd12:3456::/64',
                name = ERROR_TO_EXAMPLE_VALUE,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                vpc_id = '',
        )
        """

    def testVpcSubnet(self):
        """Test VpcSubnet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
