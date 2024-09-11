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

from oxide.models.distributionint64 import Distributionint64

class TestDistributionint64(unittest.TestCase):
    """Distributionint64 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Distributionint64:
        """Test Distributionint64
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Distributionint64`
        """
        model = Distributionint64()
        if include_optional:
            return Distributionint64(
                bins = [
                    56
                    ],
                counts = [
                    0
                    ],
                max = 56,
                min = 56,
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
                sum_of_samples = 56
            )
        else:
            return Distributionint64(
                bins = [
                    56
                    ],
                counts = [
                    0
                    ],
                squared_mean = 1.337,
                sum_of_samples = 56,
        )
        """

    def testDistributionint64(self):
        """Test Distributionint64"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
