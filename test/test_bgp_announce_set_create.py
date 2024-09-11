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

from oxide.models.bgp_announce_set_create import BgpAnnounceSetCreate

class TestBgpAnnounceSetCreate(unittest.TestCase):
    """BgpAnnounceSetCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BgpAnnounceSetCreate:
        """Test BgpAnnounceSetCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BgpAnnounceSetCreate`
        """
        model = BgpAnnounceSetCreate()
        if include_optional:
            return BgpAnnounceSetCreate(
                announcement = [
                    oxide.models.bgp_announcement_create.BgpAnnouncementCreate(
                        address_lot_block = null, 
                        network = null, )
                    ],
                description = '',
                name = ERROR_TO_EXAMPLE_VALUE
            )
        else:
            return BgpAnnounceSetCreate(
                announcement = [
                    oxide.models.bgp_announcement_create.BgpAnnouncementCreate(
                        address_lot_block = null, 
                        network = null, )
                    ],
                description = '',
                name = ERROR_TO_EXAMPLE_VALUE,
        )
        """

    def testBgpAnnounceSetCreate(self):
        """Test BgpAnnounceSetCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
