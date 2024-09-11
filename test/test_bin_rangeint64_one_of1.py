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

from oxide.models.bin_rangeint64_one_of1 import BinRangeint64OneOf1

class TestBinRangeint64OneOf1(unittest.TestCase):
    """BinRangeint64OneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangeint64OneOf1:
        """Test BinRangeint64OneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangeint64OneOf1`
        """
        model = BinRangeint64OneOf1()
        if include_optional:
            return BinRangeint64OneOf1(
                end = 56,
                start = 56,
                type = 'range'
            )
        else:
            return BinRangeint64OneOf1(
                end = 56,
                start = 56,
                type = 'range',
        )
        """

    def testBinRangeint64OneOf1(self):
        """Test BinRangeint64OneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
