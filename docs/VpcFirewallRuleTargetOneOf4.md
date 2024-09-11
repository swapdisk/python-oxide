# VpcFirewallRuleTargetOneOf4

The rule applies to a specific IP subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**IpNet**](IpNet.md) |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_target_one_of4 import VpcFirewallRuleTargetOneOf4

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleTargetOneOf4 from a JSON string
vpc_firewall_rule_target_one_of4_instance = VpcFirewallRuleTargetOneOf4.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleTargetOneOf4.to_json())

# convert the object into a dict
vpc_firewall_rule_target_one_of4_dict = vpc_firewall_rule_target_one_of4_instance.to_dict()
# create an instance of VpcFirewallRuleTargetOneOf4 from a dict
vpc_firewall_rule_target_one_of4_from_dict = VpcFirewallRuleTargetOneOf4.from_dict(vpc_firewall_rule_target_one_of4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


