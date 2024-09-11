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

from oxide.models.histogramuint8 import Histogramuint8

class TestHistogramuint8(unittest.TestCase):
    """Histogramuint8 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Histogramuint8:
        """Test Histogramuint8
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Histogramuint8`
        """
        model = Histogramuint8()
        if include_optional:
            return Histogramuint8(
                bins = [
                    oxide.models.binuint8.Binuint8(
                        count = 0, 
                        range = null, )
                    ],
                max = 0,
                min = 0,
                n_samples = 0,
                p50 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                p90 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                p99 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                squared_mean = 1.337,
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sum_of_samples = 56
            )
        else:
            return Histogramuint8(
                bins = [
                    oxide.models.binuint8.Binuint8(
                        count = 0, 
                        range = null, )
                    ],
                max = 0,
                min = 0,
                n_samples = 0,
                p50 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                p90 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                p99 = oxide.models.quantile.Quantile(
                    desired_marker_positions = [
                        1.337
                        ], 
                    marker_heights = [
                        1.337
                        ], 
                    marker_positions = [
                        0
                        ], 
                    p = 1.337, ),
                squared_mean = 1.337,
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sum_of_samples = 56,
        )
        """

    def testHistogramuint8(self):
        """Test Histogramuint8"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
