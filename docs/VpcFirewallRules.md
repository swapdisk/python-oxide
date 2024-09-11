# VpcFirewallRules

Collection of a Vpc's firewall rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[VpcFirewallRule]**](VpcFirewallRule.md) |  | 

## Example

```python
from oxide.models.vpc_firewall_rules import VpcFirewallRules

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRules from a JSON string
vpc_firewall_rules_instance = VpcFirewallRules.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRules.to_json())

# convert the object into a dict
vpc_firewall_rules_dict = vpc_firewall_rules_instance.to_dict()
# create an instance of VpcFirewallRules from a dict
vpc_firewall_rules_from_dict = VpcFirewallRules.from_dict(vpc_firewall_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


