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

from oxide.models.ssh_key_results_page import SshKeyResultsPage

class TestSshKeyResultsPage(unittest.TestCase):
    """SshKeyResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SshKeyResultsPage:
        """Test SshKeyResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SshKeyResultsPage`
        """
        model = SshKeyResultsPage()
        if include_optional:
            return SshKeyResultsPage(
                items = [
                    oxide.models.ssh_key.SshKey(
                        description = '', 
                        id = '', 
                        name = null, 
                        public_key = '', 
                        silo_user_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page = ''
            )
        else:
            return SshKeyResultsPage(
                items = [
                    oxide.models.ssh_key.SshKey(
                        description = '', 
                        id = '', 
                        name = null, 
                        public_key = '', 
                        silo_user_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testSshKeyResultsPage(self):
        """Test SshKeyResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
