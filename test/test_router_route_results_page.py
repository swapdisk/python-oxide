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

from oxide.models.router_route_results_page import RouterRouteResultsPage

class TestRouterRouteResultsPage(unittest.TestCase):
    """RouterRouteResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouterRouteResultsPage:
        """Test RouterRouteResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouterRouteResultsPage`
        """
        model = RouterRouteResultsPage()
        if include_optional:
            return RouterRouteResultsPage(
                items = [
                    oxide.models.router_route.RouterRoute(
                        description = '', 
                        destination = null, 
                        id = '', 
                        kind = null, 
                        name = null, 
                        target = null, 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        vpc_router_id = '', )
                    ],
                next_page = ''
            )
        else:
            return RouterRouteResultsPage(
                items = [
                    oxide.models.router_route.RouterRoute(
                        description = '', 
                        destination = null, 
                        id = '', 
                        kind = null, 
                        name = null, 
                        target = null, 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        vpc_router_id = '', )
                    ],
        )
        """

    def testRouterRouteResultsPage(self):
        """Test RouterRouteResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
