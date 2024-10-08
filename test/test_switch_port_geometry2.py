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

from oxide.models.switch_port_geometry2 import SwitchPortGeometry2

class TestSwitchPortGeometry2(unittest.TestCase):
    """SwitchPortGeometry2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwitchPortGeometry2:
        """Test SwitchPortGeometry2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwitchPortGeometry2`
        """
        model = SwitchPortGeometry2()
        if include_optional:
            return SwitchPortGeometry2(
            )
        else:
            return SwitchPortGeometry2(
        )
        """

    def testSwitchPortGeometry2(self):
        """Test SwitchPortGeometry2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
