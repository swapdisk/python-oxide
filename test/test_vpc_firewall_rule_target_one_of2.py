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

from oxide.models.vpc_firewall_rule_target_one_of2 import VpcFirewallRuleTargetOneOf2

class TestVpcFirewallRuleTargetOneOf2(unittest.TestCase):
    """VpcFirewallRuleTargetOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VpcFirewallRuleTargetOneOf2:
        """Test VpcFirewallRuleTargetOneOf2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VpcFirewallRuleTargetOneOf2`
        """
        model = VpcFirewallRuleTargetOneOf2()
        if include_optional:
            return VpcFirewallRuleTargetOneOf2(
                type = 'instance',
                value = ERROR_TO_EXAMPLE_VALUE
            )
        else:
            return VpcFirewallRuleTargetOneOf2(
                type = 'instance',
                value = ERROR_TO_EXAMPLE_VALUE,
        )
        """

    def testVpcFirewallRuleTargetOneOf2(self):
        """Test VpcFirewallRuleTargetOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
