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

from oxide.models.cumulativeuint64 import Cumulativeuint64

class TestCumulativeuint64(unittest.TestCase):
    """Cumulativeuint64 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Cumulativeuint64:
        """Test Cumulativeuint64
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Cumulativeuint64`
        """
        model = Cumulativeuint64()
        if include_optional:
            return Cumulativeuint64(
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                value = 0
            )
        else:
            return Cumulativeuint64(
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                value = 0,
        )
        """

    def testCumulativeuint64(self):
        """Test Cumulativeuint64"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
