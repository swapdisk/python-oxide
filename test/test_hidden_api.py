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

from oxide.api.hidden_api import HiddenApi


class TestHiddenApi(unittest.TestCase):
    """HiddenApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HiddenApi()

    def tearDown(self) -> None:
        pass

    def test_device_access_token(self) -> None:
        """Test case for device_access_token

        Request a device access token
        """
        pass

    def test_device_auth_confirm(self) -> None:
        """Test case for device_auth_confirm

        Confirm an OAuth 2.0 Device Authorization Grant
        """
        pass

    def test_device_auth_request(self) -> None:
        """Test case for device_auth_request

        Start an OAuth 2.0 Device Authorization Grant
        """
        pass

    def test_logout(self) -> None:
        """Test case for logout

        Log user out of web console by deleting session on client and server
        """
        pass

    def test_probe_create(self) -> None:
        """Test case for probe_create

        Create instrumentation probe
        """
        pass

    def test_probe_delete(self) -> None:
        """Test case for probe_delete

        Delete instrumentation probe
        """
        pass

    def test_probe_list(self) -> None:
        """Test case for probe_list

        List instrumentation probes
        """
        pass

    def test_probe_view(self) -> None:
        """Test case for probe_view

        View instrumentation probe
        """
        pass


if __name__ == '__main__':
    unittest.main()
