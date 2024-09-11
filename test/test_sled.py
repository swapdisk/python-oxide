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

from oxide.models.sled import Sled

class TestSled(unittest.TestCase):
    """Sled unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Sled:
        """Test Sled
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Sled`
        """
        model = Sled()
        if include_optional:
            return Sled(
                baseboard = oxide.models.baseboard.Baseboard(
                    part = '', 
                    revision = 0, 
                    serial = '', ),
                id = '',
                policy = None,
                rack_id = '',
                state = None,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usable_hardware_threads = 0,
                usable_physical_ram = 0
            )
        else:
            return Sled(
                baseboard = oxide.models.baseboard.Baseboard(
                    part = '', 
                    revision = 0, 
                    serial = '', ),
                id = '',
                policy = None,
                rack_id = '',
                state = None,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usable_hardware_threads = 0,
                usable_physical_ram = 0,
        )
        """

    def testSled(self):
        """Test Sled"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
