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

from oxide.models.oxql_query_result import OxqlQueryResult

class TestOxqlQueryResult(unittest.TestCase):
    """OxqlQueryResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OxqlQueryResult:
        """Test OxqlQueryResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OxqlQueryResult`
        """
        model = OxqlQueryResult()
        if include_optional:
            return OxqlQueryResult(
                tables = [
                    oxide.models.table.Table(
                        name = '', 
                        timeseries = {
                            'key' : oxide.models.timeseries.Timeseries(
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
                                        ], ), )
                            }, )
                    ]
            )
        else:
            return OxqlQueryResult(
                tables = [
                    oxide.models.table.Table(
                        name = '', 
                        timeseries = {
                            'key' : oxide.models.timeseries.Timeseries(
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
                                        ], ), )
                            }, )
                    ],
        )
        """

    def testOxqlQueryResult(self):
        """Test OxqlQueryResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
