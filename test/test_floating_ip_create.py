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

from oxide.models.floating_ip_create import FloatingIpCreate

class TestFloatingIpCreate(unittest.TestCase):
    """FloatingIpCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FloatingIpCreate:
        """Test FloatingIpCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FloatingIpCreate`
        """
        model = FloatingIpCreate()
        if include_optional:
            return FloatingIpCreate(
                description = '',
                ip = '',
                name = ERROR_TO_EXAMPLE_VALUE,
                pool = None
            )
        else:
            return FloatingIpCreate(
                description = '',
                name = ERROR_TO_EXAMPLE_VALUE,
        )
        """

    def testFloatingIpCreate(self):
        """Test FloatingIpCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
