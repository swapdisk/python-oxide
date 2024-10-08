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

from oxide.models.field_value_one_of4 import FieldValueOneOf4

class TestFieldValueOneOf4(unittest.TestCase):
    """FieldValueOneOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldValueOneOf4:
        """Test FieldValueOneOf4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldValueOneOf4`
        """
        model = FieldValueOneOf4()
        if include_optional:
            return FieldValueOneOf4(
                type = 'u16',
                value = 0
            )
        else:
            return FieldValueOneOf4(
                type = 'u16',
                value = 0,
        )
        """

    def testFieldValueOneOf4(self):
        """Test FieldValueOneOf4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
