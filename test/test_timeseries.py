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

from oxide.models.timeseries import Timeseries

class TestTimeseries(unittest.TestCase):
    """Timeseries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Timeseries:
        """Test Timeseries
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Timeseries`
        """
        model = Timeseries()
        if include_optional:
            return Timeseries(
                fields = {
                    'key' : null
                    },
                points = oxide.models.points.Points(
                    start_times = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], 
                    timestamps = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], 
                    values = [
                        oxide.models.values.Values(
                            metric_type = null, 
                            values = null, )
                        ], )
            )
        else:
            return Timeseries(
                fields = {
                    'key' : null
                    },
                points = oxide.models.points.Points(
                    start_times = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], 
                    timestamps = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], 
                    values = [
                        oxide.models.values.Values(
                            metric_type = null, 
                            values = null, )
                        ], ),
        )
        """

    def testTimeseries(self):
        """Test Timeseries"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
