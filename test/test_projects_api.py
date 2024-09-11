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

from oxide.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_project_create(self) -> None:
        """Test case for project_create

        Create project
        """
        pass

    def test_project_delete(self) -> None:
        """Test case for project_delete

        Delete project
        """
        pass

    def test_project_ip_pool_list(self) -> None:
        """Test case for project_ip_pool_list

        List IP pools
        """
        pass

    def test_project_ip_pool_view(self) -> None:
        """Test case for project_ip_pool_view

        Fetch IP pool
        """
        pass

    def test_project_list(self) -> None:
        """Test case for project_list

        List projects
        """
        pass

    def test_project_policy_update(self) -> None:
        """Test case for project_policy_update

        Update project's IAM policy
        """
        pass

    def test_project_policy_view(self) -> None:
        """Test case for project_policy_view

        Fetch project's IAM policy
        """
        pass

    def test_project_update(self) -> None:
        """Test case for project_update

        Update a project
        """
        pass

    def test_project_view(self) -> None:
        """Test case for project_view

        Fetch project
        """
        pass


if __name__ == '__main__':
    unittest.main()
