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

from oxide.models.instance_state import InstanceState

class TestInstanceState(unittest.TestCase):
    """InstanceState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstanceState:
        """Test InstanceState
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstanceState`
        """
        model = InstanceState()
        if include_optional:
            return InstanceState(
            )
        else:
            return InstanceState(
        )
        """

    def testInstanceState(self):
        """Test InstanceState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
