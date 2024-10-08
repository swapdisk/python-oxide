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

from oxide.models.idp_metadata_source_one_of1 import IdpMetadataSourceOneOf1

class TestIdpMetadataSourceOneOf1(unittest.TestCase):
    """IdpMetadataSourceOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdpMetadataSourceOneOf1:
        """Test IdpMetadataSourceOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdpMetadataSourceOneOf1`
        """
        model = IdpMetadataSourceOneOf1()
        if include_optional:
            return IdpMetadataSourceOneOf1(
                data = '',
                type = 'base64_encoded_xml'
            )
        else:
            return IdpMetadataSourceOneOf1(
                data = '',
                type = 'base64_encoded_xml',
        )
        """

    def testIdpMetadataSourceOneOf1(self):
        """Test IdpMetadataSourceOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
