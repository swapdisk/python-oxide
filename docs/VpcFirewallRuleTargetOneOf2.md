# VpcFirewallRuleTargetOneOf2

The rule applies to this specific instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.vpc_firewall_rule_target_one_of2 import VpcFirewallRuleTargetOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleTargetOneOf2 from a JSON string
vpc_firewall_rule_target_one_of2_instance = VpcFirewallRuleTargetOneOf2.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleTargetOneOf2.to_json())

# convert the object into a dict
vpc_firewall_rule_target_one_of2_dict = vpc_firewall_rule_target_one_of2_instance.to_dict()
# create an instance of VpcFirewallRuleTargetOneOf2 from a dict
vpc_firewall_rule_target_one_of2_from_dict = VpcFirewallRuleTargetOneOf2.from_dict(vpc_firewall_rule_target_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


