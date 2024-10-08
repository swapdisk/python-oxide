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

from oxide.models.datum_one_of27 import DatumOneOf27

class TestDatumOneOf27(unittest.TestCase):
    """DatumOneOf27 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatumOneOf27:
        """Test DatumOneOf27
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatumOneOf27`
        """
        model = DatumOneOf27()
        if include_optional:
            return DatumOneOf27(
                datum = oxide.models.missing_datum.MissingDatum(
                    datum_type = 'bool', 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                type = 'missing'
            )
        else:
            return DatumOneOf27(
                datum = oxide.models.missing_datum.MissingDatum(
                    datum_type = 'bool', 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                type = 'missing',
        )
        """

    def testDatumOneOf27(self):
        """Test DatumOneOf27"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
