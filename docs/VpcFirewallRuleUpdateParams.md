# VpcFirewallRuleUpdateParams

Updated list of firewall rules. Will replace all existing rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[VpcFirewallRuleUpdate]**](VpcFirewallRuleUpdate.md) |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_update_params import VpcFirewallRuleUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleUpdateParams from a JSON string
vpc_firewall_rule_update_params_instance = VpcFirewallRuleUpdateParams.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleUpdateParams.to_json())

# convert the object into a dict
vpc_firewall_rule_update_params_dict = vpc_firewall_rule_update_params_instance.to_dict()
# create an instance of VpcFirewallRuleUpdateParams from a dict
vpc_firewall_rule_update_params_from_dict = VpcFirewallRuleUpdateParams.from_dict(vpc_firewall_rule_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


