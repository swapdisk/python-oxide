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

from oxide.models.switch_port_results_page import SwitchPortResultsPage

class TestSwitchPortResultsPage(unittest.TestCase):
    """SwitchPortResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwitchPortResultsPage:
        """Test SwitchPortResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwitchPortResultsPage`
        """
        model = SwitchPortResultsPage()
        if include_optional:
            return SwitchPortResultsPage(
                items = [
                    oxide.models.switch_port.SwitchPort(
                        id = '', 
                        port_name = '', 
                        port_settings_id = '', 
                        rack_id = '', 
                        switch_location = '', )
                    ],
                next_page = ''
            )
        else:
            return SwitchPortResultsPage(
                items = [
                    oxide.models.switch_port.SwitchPort(
                        id = '', 
                        port_name = '', 
                        port_settings_id = '', 
                        rack_id = '', 
                        switch_location = '', )
                    ],
        )
        """

    def testSwitchPortResultsPage(self):
        """Test SwitchPortResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
