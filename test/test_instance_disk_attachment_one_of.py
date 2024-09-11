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

from oxide.models.instance_disk_attachment_one_of import InstanceDiskAttachmentOneOf

class TestInstanceDiskAttachmentOneOf(unittest.TestCase):
    """InstanceDiskAttachmentOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstanceDiskAttachmentOneOf:
        """Test InstanceDiskAttachmentOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstanceDiskAttachmentOneOf`
        """
        model = InstanceDiskAttachmentOneOf()
        if include_optional:
            return InstanceDiskAttachmentOneOf(
                description = '',
                disk_source = None,
                name = ERROR_TO_EXAMPLE_VALUE,
                size = 0,
                type = 'create'
            )
        else:
            return InstanceDiskAttachmentOneOf(
                description = '',
                disk_source = None,
                name = ERROR_TO_EXAMPLE_VALUE,
                size = 0,
                type = 'create',
        )
        """

    def testInstanceDiskAttachmentOneOf(self):
        """Test InstanceDiskAttachmentOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
