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

from oxide.models.sled_instance_results_page import SledInstanceResultsPage

class TestSledInstanceResultsPage(unittest.TestCase):
    """SledInstanceResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SledInstanceResultsPage:
        """Test SledInstanceResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SledInstanceResultsPage`
        """
        model = SledInstanceResultsPage()
        if include_optional:
            return SledInstanceResultsPage(
                items = ERROR_TO_EXAMPLE_VALUE,
                next_page = ''
            )
        else:
            return SledInstanceResultsPage(
                items = ERROR_TO_EXAMPLE_VALUE,
        )
        """

    def testSledInstanceResultsPage(self):
        """Test SledInstanceResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
