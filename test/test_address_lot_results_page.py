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

from oxide.models.address_lot_results_page import AddressLotResultsPage

class TestAddressLotResultsPage(unittest.TestCase):
    """AddressLotResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressLotResultsPage:
        """Test AddressLotResultsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressLotResultsPage`
        """
        model = AddressLotResultsPage()
        if include_optional:
            return AddressLotResultsPage(
                items = [
                    oxide.models.address_lot.AddressLot(
                        description = '', 
                        id = '', 
                        kind = null, 
                        name = null, 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page = ''
            )
        else:
            return AddressLotResultsPage(
                items = [
                    oxide.models.address_lot.AddressLot(
                        description = '', 
                        id = '', 
                        kind = null, 
                        name = null, 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testAddressLotResultsPage(self):
        """Test AddressLotResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
