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

from oxide.models.vpc_results_page import VpcResultsPage

class TestVpcResultsPage(unittest.TestCase):
    """VpcResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VpcResultsPage:
        """Test VpcResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VpcResultsPage`
        """
        model = VpcResultsPage()
        if include_optional:
            return VpcResultsPage(
                items = [
                    oxide.models.vpc.Vpc(
                        description = '', 
                        dns_name = null, 
                        id = '', 
                        ipv6_prefix = null, 
                        name = null, 
                        project_id = '', 
                        system_router_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page = ''
            )
        else:
            return VpcResultsPage(
                items = [
                    oxide.models.vpc.Vpc(
                        description = '', 
                        dns_name = null, 
                        id = '', 
                        ipv6_prefix = null, 
                        name = null, 
                        project_id = '', 
                        system_router_id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testVpcResultsPage(self):
        """Test VpcResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
