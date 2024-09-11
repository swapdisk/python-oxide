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

from oxide.models.datum_one_of import DatumOneOf

class TestDatumOneOf(unittest.TestCase):
    """DatumOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatumOneOf:
        """Test DatumOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatumOneOf`
        """
        model = DatumOneOf()
        if include_optional:
            return DatumOneOf(
                datum = True,
                type = 'bool'
            )
        else:
            return DatumOneOf(
                datum = True,
                type = 'bool',
        )
        """

    def testDatumOneOf(self):
        """Test DatumOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
