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

from oxide.models.loopback_address import LoopbackAddress

class TestLoopbackAddress(unittest.TestCase):
    """LoopbackAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoopbackAddress:
        """Test LoopbackAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoopbackAddress`
        """
        model = LoopbackAddress()
        if include_optional:
            return LoopbackAddress(
                address = None,
                address_lot_block_id = '',
                id = '',
                rack_id = '',
                switch_location = ''
            )
        else:
            return LoopbackAddress(
                address = None,
                address_lot_block_id = '',
                id = '',
                rack_id = '',
                switch_location = '',
        )
        """

    def testLoopbackAddress(self):
        """Test LoopbackAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
