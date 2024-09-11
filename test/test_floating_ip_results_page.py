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

from oxide.models.floating_ip_results_page import FloatingIpResultsPage

class TestFloatingIpResultsPage(unittest.TestCase):
    """FloatingIpResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FloatingIpResultsPage:
        """Test FloatingIpResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FloatingIpResultsPage`
        """
        model = FloatingIpResultsPage()
        if include_optional:
            return FloatingIpResultsPage(
                items = [
                    oxide.models.floating_ip.FloatingIp(
                        description = '', 
                        id = '', 
                        instance_id = '', 
                        ip = '', 
                        ip_pool_id = '', 
                        name = null, 
                        project_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page = ''
            )
        else:
            return FloatingIpResultsPage(
                items = [
                    oxide.models.floating_ip.FloatingIp(
                        description = '', 
                        id = '', 
                        instance_id = '', 
                        ip = '', 
                        ip_pool_id = '', 
                        name = null, 
                        project_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testFloatingIpResultsPage(self):
        """Test FloatingIpResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
