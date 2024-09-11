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

from oxide.models.bin_rangeint8 import BinRangeint8

class TestBinRangeint8(unittest.TestCase):
    """BinRangeint8 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangeint8:
        """Test BinRangeint8
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangeint8`
        """
        model = BinRangeint8()
        if include_optional:
            return BinRangeint8(
                end = 56,
                type = 'range_to',
                start = 56
            )
        else:
            return BinRangeint8(
                end = 56,
                type = 'range_to',
                start = 56,
        )
        """

    def testBinRangeint8(self):
        """Test BinRangeint8"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
