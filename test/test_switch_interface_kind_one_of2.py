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

from oxide.models.switch_interface_kind_one_of2 import SwitchInterfaceKindOneOf2

class TestSwitchInterfaceKindOneOf2(unittest.TestCase):
    """SwitchInterfaceKindOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwitchInterfaceKindOneOf2:
        """Test SwitchInterfaceKindOneOf2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwitchInterfaceKindOneOf2`
        """
        model = SwitchInterfaceKindOneOf2()
        if include_optional:
            return SwitchInterfaceKindOneOf2(
                type = 'loopback'
            )
        else:
            return SwitchInterfaceKindOneOf2(
                type = 'loopback',
        )
        """

    def testSwitchInterfaceKindOneOf2(self):
        """Test SwitchInterfaceKindOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
