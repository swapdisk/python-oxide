# VpcFirewallRuleHostFilterOneOf1

The rule applies to traffic from/to all instances in the VPC Subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.vpc_firewall_rule_host_filter_one_of1 import VpcFirewallRuleHostFilterOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleHostFilterOneOf1 from a JSON string
vpc_firewall_rule_host_filter_one_of1_instance = VpcFirewallRuleHostFilterOneOf1.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleHostFilterOneOf1.to_json())

# convert the object into a dict
vpc_firewall_rule_host_filter_one_of1_dict = vpc_firewall_rule_host_filter_one_of1_instance.to_dict()
# create an instance of VpcFirewallRuleHostFilterOneOf1 from a dict
vpc_firewall_rule_host_filter_one_of1_from_dict = VpcFirewallRuleHostFilterOneOf1.from_dict(vpc_firewall_rule_host_filter_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


