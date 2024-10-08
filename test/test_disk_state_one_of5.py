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

from oxide.models.disk_state_one_of5 import DiskStateOneOf5

class TestDiskStateOneOf5(unittest.TestCase):
    """DiskStateOneOf5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiskStateOneOf5:
        """Test DiskStateOneOf5
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiskStateOneOf5`
        """
        model = DiskStateOneOf5()
        if include_optional:
            return DiskStateOneOf5(
                state = 'finalizing'
            )
        else:
            return DiskStateOneOf5(
                state = 'finalizing',
        )
        """

    def testDiskStateOneOf5(self):
        """Test DiskStateOneOf5"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
