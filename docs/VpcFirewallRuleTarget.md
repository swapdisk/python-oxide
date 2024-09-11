# VpcFirewallRuleTarget

A `VpcFirewallRuleTarget` is used to specify the set of instances to which a firewall rule applies. You can target instances directly by name, or specify a VPC, VPC subnet, IP, or IP subnet, which will apply the rule to traffic going to all matching instances. Targets are additive: the rule applies to instances matching ANY target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**IpNet**](IpNet.md) |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_target import VpcFirewallRuleTarget

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleTarget from a JSON string
vpc_firewall_rule_target_instance = VpcFirewallRuleTarget.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleTarget.to_json())

# convert the object into a dict
vpc_firewall_rule_target_dict = vpc_firewall_rule_target_instance.to_dict()
# create an instance of VpcFirewallRuleTarget from a dict
vpc_firewall_rule_target_from_dict = VpcFirewallRuleTarget.from_dict(vpc_firewall_rule_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


