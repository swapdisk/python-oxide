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

from oxide.models.datum_one_of22 import DatumOneOf22

class TestDatumOneOf22(unittest.TestCase):
    """DatumOneOf22 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatumOneOf22:
        """Test DatumOneOf22
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatumOneOf22`
        """
        model = DatumOneOf22()
        if include_optional:
            return DatumOneOf22(
                datum = oxide.models.histogramuint32.Histogramuint32(
                    bins = [
                        oxide.models.binuint32.Binuint32(
                            count = 0, 
                            range = null, )
                        ], 
                    max = 0, 
                    min = 0, 
                    n_samples = 0, 
                    p50 = null, 
                    p90 = null, 
                    p99 = null, 
                    squared_mean = 1.337, 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    sum_of_samples = 56, ),
                type = 'histogram_u32'
            )
        else:
            return DatumOneOf22(
                datum = oxide.models.histogramuint32.Histogramuint32(
                    bins = [
                        oxide.models.binuint32.Binuint32(
                            count = 0, 
                            range = null, )
                        ], 
                    max = 0, 
                    min = 0, 
                    n_samples = 0, 
                    p50 = null, 
                    p90 = null, 
                    p99 = null, 
                    squared_mean = 1.337, 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    sum_of_samples = 56, ),
                type = 'histogram_u32',
        )
        """

    def testDatumOneOf22(self):
        """Test DatumOneOf22"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
