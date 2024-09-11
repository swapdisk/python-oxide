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

from oxide.models.image_source_one_of1 import ImageSourceOneOf1

class TestImageSourceOneOf1(unittest.TestCase):
    """ImageSourceOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageSourceOneOf1:
        """Test ImageSourceOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageSourceOneOf1`
        """
        model = ImageSourceOneOf1()
        if include_optional:
            return ImageSourceOneOf1(
                type = 'you_can_boot_anything_as_long_as_its_alpine'
            )
        else:
            return ImageSourceOneOf1(
                type = 'you_can_boot_anything_as_long_as_its_alpine',
        )
        """

    def testImageSourceOneOf1(self):
        """Test ImageSourceOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
