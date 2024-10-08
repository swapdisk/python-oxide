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

from oxide.models.vpc_subnet_create import VpcSubnetCreate

class TestVpcSubnetCreate(unittest.TestCase):
    """VpcSubnetCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VpcSubnetCreate:
        """Test VpcSubnetCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VpcSubnetCreate`
        """
        model = VpcSubnetCreate()
        if include_optional:
            return VpcSubnetCreate(
                custom_router = None,
                description = '',
                ipv4_block = '192.168.1.0/24',
                ipv6_block = 'fd12:3456::/64',
                name = ERROR_TO_EXAMPLE_VALUE
            )
        else:
            return VpcSubnetCreate(
                description = '',
                ipv4_block = '192.168.1.0/24',
                name = ERROR_TO_EXAMPLE_VALUE,
        )
        """

    def testVpcSubnetCreate(self):
        """Test VpcSubnetCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
