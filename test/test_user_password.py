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

from oxide.models.user_password import UserPassword

class TestUserPassword(unittest.TestCase):
    """UserPassword unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPassword:
        """Test UserPassword
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPassword`
        """
        model = UserPassword()
        if include_optional:
            return UserPassword(
                mode = 'login_disallowed',
                value = ''
            )
        else:
            return UserPassword(
                mode = 'login_disallowed',
                value = '',
        )
        """

    def testUserPassword(self):
        """Test UserPassword"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
