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

from oxide.models.snapshot_results_page import SnapshotResultsPage

class TestSnapshotResultsPage(unittest.TestCase):
    """SnapshotResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotResultsPage:
        """Test SnapshotResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotResultsPage`
        """
        model = SnapshotResultsPage()
        if include_optional:
            return SnapshotResultsPage(
                items = [
                    oxide.models.snapshot.Snapshot(
                        description = '', 
                        disk_id = '', 
                        id = '', 
                        name = null, 
                        project_id = '', 
                        size = 0, 
                        state = 'creating', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page = ''
            )
        else:
            return SnapshotResultsPage(
                items = [
                    oxide.models.snapshot.Snapshot(
                        description = '', 
                        disk_id = '', 
                        id = '', 
                        name = null, 
                        project_id = '', 
                        size = 0, 
                        state = 'creating', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testSnapshotResultsPage(self):
        """Test SnapshotResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
