# VpcFirewallRuleHostFilterOneOf3

The rule applies to traffic from/to a specific IP address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_host_filter_one_of3 import VpcFirewallRuleHostFilterOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleHostFilterOneOf3 from a JSON string
vpc_firewall_rule_host_filter_one_of3_instance = VpcFirewallRuleHostFilterOneOf3.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleHostFilterOneOf3.to_json())

# convert the object into a dict
vpc_firewall_rule_host_filter_one_of3_dict = vpc_firewall_rule_host_filter_one_of3_instance.to_dict()
# create an instance of VpcFirewallRuleHostFilterOneOf3 from a dict
vpc_firewall_rule_host_filter_one_of3_from_dict = VpcFirewallRuleHostFilterOneOf3.from_dict(vpc_firewall_rule_host_filter_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


