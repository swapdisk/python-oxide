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

from oxide.models.bin_rangefloat_one_of1 import BinRangefloatOneOf1

class TestBinRangefloatOneOf1(unittest.TestCase):
    """BinRangefloatOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangefloatOneOf1:
        """Test BinRangefloatOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangefloatOneOf1`
        """
        model = BinRangefloatOneOf1()
        if include_optional:
            return BinRangefloatOneOf1(
                end = 1.337,
                start = 1.337,
                type = 'range'
            )
        else:
            return BinRangefloatOneOf1(
                end = 1.337,
                start = 1.337,
                type = 'range',
        )
        """

    def testBinRangefloatOneOf1(self):
        """Test BinRangefloatOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
