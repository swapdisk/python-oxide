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

from oxide.models.allow_list_update import AllowListUpdate

class TestAllowListUpdate(unittest.TestCase):
    """AllowListUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllowListUpdate:
        """Test AllowListUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllowListUpdate`
        """
        model = AllowListUpdate()
        if include_optional:
            return AllowListUpdate(
                allowed_ips = None
            )
        else:
            return AllowListUpdate(
                allowed_ips = None,
        )
        """

    def testAllowListUpdate(self):
        """Test AllowListUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
