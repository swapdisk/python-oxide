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

from oxide.models.datum_one_of6 import DatumOneOf6

class TestDatumOneOf6(unittest.TestCase):
    """DatumOneOf6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatumOneOf6:
        """Test DatumOneOf6
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatumOneOf6`
        """
        model = DatumOneOf6()
        if include_optional:
            return DatumOneOf6(
                datum = 0,
                type = 'u32'
            )
        else:
            return DatumOneOf6(
                datum = 0,
                type = 'u32',
        )
        """

    def testDatumOneOf6(self):
        """Test DatumOneOf6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
