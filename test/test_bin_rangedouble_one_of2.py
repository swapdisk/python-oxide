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

from oxide.models.bin_rangedouble_one_of2 import BinRangedoubleOneOf2

class TestBinRangedoubleOneOf2(unittest.TestCase):
    """BinRangedoubleOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BinRangedoubleOneOf2:
        """Test BinRangedoubleOneOf2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BinRangedoubleOneOf2`
        """
        model = BinRangedoubleOneOf2()
        if include_optional:
            return BinRangedoubleOneOf2(
                start = 1.337,
                type = 'range_from'
            )
        else:
            return BinRangedoubleOneOf2(
                start = 1.337,
                type = 'range_from',
        )
        """

    def testBinRangedoubleOneOf2(self):
        """Test BinRangedoubleOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
