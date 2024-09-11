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

from oxide.models.silo_role_policy import SiloRolePolicy

class TestSiloRolePolicy(unittest.TestCase):
    """SiloRolePolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiloRolePolicy:
        """Test SiloRolePolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiloRolePolicy`
        """
        model = SiloRolePolicy()
        if include_optional:
            return SiloRolePolicy(
                role_assignments = [
                    oxide.models.silo_role_role_assignment.SiloRoleRoleAssignment(
                        identity_id = '', 
                        identity_type = 'silo_user', 
                        role_name = 'admin', )
                    ]
            )
        else:
            return SiloRolePolicy(
                role_assignments = [
                    oxide.models.silo_role_role_assignment.SiloRoleRoleAssignment(
                        identity_id = '', 
                        identity_type = 'silo_user', 
                        role_name = 'admin', )
                    ],
        )
        """

    def testSiloRolePolicy(self):
        """Test SiloRolePolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
