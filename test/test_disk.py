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

from oxide.models.disk import Disk

class TestDisk(unittest.TestCase):
    """Disk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Disk:
        """Test Disk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Disk`
        """
        model = Disk()
        if include_optional:
            return Disk(
                block_size = 0,
                description = '',
                device_path = '',
                id = '',
                image_id = '',
                name = ERROR_TO_EXAMPLE_VALUE,
                project_id = '',
                size = 0,
                snapshot_id = '',
                state = None,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Disk(
                block_size = 0,
                description = '',
                device_path = '',
                id = '',
                name = ERROR_TO_EXAMPLE_VALUE,
                project_id = '',
                size = 0,
                state = None,
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDisk(self):
        """Test Disk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
