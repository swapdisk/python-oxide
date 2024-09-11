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

from oxide.models.bin_rangeint8_one_of2 import BinRangeint8OneOf2

class TestBinRangeint8OneOf2(unittest.TestCase):
    """BinRangeint8OneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangeint8OneOf2:
        """Test BinRangeint8OneOf2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangeint8OneOf2`
        """
        model = BinRangeint8OneOf2()
        if include_optional:
            return BinRangeint8OneOf2(
                start = 56,
                type = 'range_from'
            )
        else:
            return BinRangeint8OneOf2(
                start = 56,
                type = 'range_from',
        )
        """

    def testBinRangeint8OneOf2(self):
        """Test BinRangeint8OneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
