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

from oxide.api.system_networking_api import SystemNetworkingApi


class TestSystemNetworkingApi(unittest.TestCase):
    """SystemNetworkingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemNetworkingApi()

    def tearDown(self) -> None:
        pass

    def test_networking_address_lot_block_list(self) -> None:
        """Test case for networking_address_lot_block_list

        List blocks in address lot
        """
        pass

    def test_networking_address_lot_create(self) -> None:
        """Test case for networking_address_lot_create

        Create address lot
        """
        pass

    def test_networking_address_lot_delete(self) -> None:
        """Test case for networking_address_lot_delete

        Delete address lot
        """
        pass

    def test_networking_address_lot_list(self) -> None:
        """Test case for networking_address_lot_list

        List address lots
        """
        pass

    def test_networking_allow_list_update(self) -> None:
        """Test case for networking_allow_list_update

        Update user-facing services IP allowlist
        """
        pass

    def test_networking_allow_list_view(self) -> None:
        """Test case for networking_allow_list_view

        Get user-facing services IP allowlist
        """
        pass

    def test_networking_bfd_disable(self) -> None:
        """Test case for networking_bfd_disable

        Disable a BFD session
        """
        pass

    def test_networking_bfd_enable(self) -> None:
        """Test case for networking_bfd_enable

        Enable a BFD session
        """
        pass

    def test_networking_bfd_status(self) -> None:
        """Test case for networking_bfd_status

        Get BFD status
        """
        pass

    def test_networking_bgp_announce_set_delete(self) -> None:
        """Test case for networking_bgp_announce_set_delete

        Delete BGP announce set
        """
        pass

    def test_networking_bgp_announce_set_list(self) -> None:
        """Test case for networking_bgp_announce_set_list

        List BGP announce sets
        """
        pass

    def test_networking_bgp_announce_set_update(self) -> None:
        """Test case for networking_bgp_announce_set_update

        Update BGP announce set
        """
        pass

    def test_networking_bgp_announcement_list(self) -> None:
        """Test case for networking_bgp_announcement_list

        Get originated routes for a specified BGP announce set
        """
        pass

    def test_networking_bgp_config_create(self) -> None:
        """Test case for networking_bgp_config_create

        Create new BGP configuration
        """
        pass

    def test_networking_bgp_config_delete(self) -> None:
        """Test case for networking_bgp_config_delete

        Delete BGP configuration
        """
        pass

    def test_networking_bgp_config_list(self) -> None:
        """Test case for networking_bgp_config_list

        List BGP configurations
        """
        pass

    def test_networking_bgp_exported(self) -> None:
        """Test case for networking_bgp_exported

        Get BGP exported routes
        """
        pass

    def test_networking_bgp_imported_routes_ipv4(self) -> None:
        """Test case for networking_bgp_imported_routes_ipv4

        Get imported IPv4 BGP routes
        """
        pass

    def test_networking_bgp_message_history(self) -> None:
        """Test case for networking_bgp_message_history

        Get BGP router message history
        """
        pass

    def test_networking_bgp_status(self) -> None:
        """Test case for networking_bgp_status

        Get BGP peer status
        """
        pass

    def test_networking_loopback_address_create(self) -> None:
        """Test case for networking_loopback_address_create

        Create loopback address
        """
        pass

    def test_networking_loopback_address_delete(self) -> None:
        """Test case for networking_loopback_address_delete

        Delete loopback address
        """
        pass

    def test_networking_loopback_address_list(self) -> None:
        """Test case for networking_loopback_address_list

        List loopback addresses
        """
        pass

    def test_networking_switch_port_settings_create(self) -> None:
        """Test case for networking_switch_port_settings_create

        Create switch port settings
        """
        pass

    def test_networking_switch_port_settings_delete(self) -> None:
        """Test case for networking_switch_port_settings_delete

        Delete switch port settings
        """
        pass

    def test_networking_switch_port_settings_list(self) -> None:
        """Test case for networking_switch_port_settings_list

        List switch port settings
        """
        pass

    def test_networking_switch_port_settings_view(self) -> None:
        """Test case for networking_switch_port_settings_view

        Get information about switch port
        """
        pass


if __name__ == '__main__':
    unittest.main()
