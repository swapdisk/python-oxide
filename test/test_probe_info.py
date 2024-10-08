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

from oxide.models.probe_info import ProbeInfo

class TestProbeInfo(unittest.TestCase):
    """ProbeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProbeInfo:
        """Test ProbeInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProbeInfo`
        """
        model = ProbeInfo()
        if include_optional:
            return ProbeInfo(
                external_ips = [
                    oxide.models.probe_external_ip.ProbeExternalIp(
                        first_port = 0, 
                        ip = '', 
                        kind = 'snat', 
                        last_port = 0, )
                    ],
                id = '',
                interface = ERROR_TO_EXAMPLE_VALUE,
                name = ERROR_TO_EXAMPLE_VALUE,
                sled = ''
            )
        else:
            return ProbeInfo(
                external_ips = [
                    oxide.models.probe_external_ip.ProbeExternalIp(
                        first_port = 0, 
                        ip = '', 
                        kind = 'snat', 
                        last_port = 0, )
                    ],
                id = '',
                interface = ERROR_TO_EXAMPLE_VALUE,
                name = ERROR_TO_EXAMPLE_VALUE,
                sled = '',
        )
        """

    def testProbeInfo(self):
        """Test ProbeInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
