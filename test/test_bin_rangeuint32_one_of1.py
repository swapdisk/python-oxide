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

from oxide.models.bin_rangeuint32_one_of1 import BinRangeuint32OneOf1

class TestBinRangeuint32OneOf1(unittest.TestCase):
    """BinRangeuint32OneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangeuint32OneOf1:
        """Test BinRangeuint32OneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangeuint32OneOf1`
        """
        model = BinRangeuint32OneOf1()
        if include_optional:
            return BinRangeuint32OneOf1(
                end = 0,
                start = 0,
                type = 'range'
            )
        else:
            return BinRangeuint32OneOf1(
                end = 0,
                start = 0,
                type = 'range',
        )
        """

    def testBinRangeuint32OneOf1(self):
        """Test BinRangeuint32OneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
