# VpcFirewallRuleTargetOneOf3

The rule applies to a specific IP address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_target_one_of3 import VpcFirewallRuleTargetOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleTargetOneOf3 from a JSON string
vpc_firewall_rule_target_one_of3_instance = VpcFirewallRuleTargetOneOf3.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleTargetOneOf3.to_json())

# convert the object into a dict
vpc_firewall_rule_target_one_of3_dict = vpc_firewall_rule_target_one_of3_instance.to_dict()
# create an instance of VpcFirewallRuleTargetOneOf3 from a dict
vpc_firewall_rule_target_one_of3_from_dict = VpcFirewallRuleTargetOneOf3.from_dict(vpc_firewall_rule_target_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


