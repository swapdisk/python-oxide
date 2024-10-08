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

from oxide.models.datum_one_of16 import DatumOneOf16

class TestDatumOneOf16(unittest.TestCase):
    """DatumOneOf16 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatumOneOf16:
        """Test DatumOneOf16
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatumOneOf16`
        """
        model = DatumOneOf16()
        if include_optional:
            return DatumOneOf16(
                datum = oxide.models.cumulativedouble.Cumulativedouble(
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    value = 1.337, ),
                type = 'cumulative_f64'
            )
        else:
            return DatumOneOf16(
                datum = oxide.models.cumulativedouble.Cumulativedouble(
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    value = 1.337, ),
                type = 'cumulative_f64',
        )
        """

    def testDatumOneOf16(self):
        """Test DatumOneOf16"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
