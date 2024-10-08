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

from oxide.models.route import Route

class TestRoute(unittest.TestCase):
    """Route unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Route:
        """Test Route
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Route`
        """
        model = Route()
        if include_optional:
            return Route(
                dst = None,
                gw = '',
                local_pref = 0,
                vid = 0
            )
        else:
            return Route(
                dst = None,
                gw = '',
        )
        """

    def testRoute(self):
        """Test Route"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
