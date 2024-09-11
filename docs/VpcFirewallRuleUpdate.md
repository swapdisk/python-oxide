# VpcFirewallRuleUpdate

A single rule in a VPC firewall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**VpcFirewallRuleAction**](VpcFirewallRuleAction.md) | Whether traffic matching the rule should be allowed or dropped | 
**description** | **str** | Human-readable free-form text about a resource | 
**direction** | [**VpcFirewallRuleDirection**](VpcFirewallRuleDirection.md) | Whether this rule is for incoming or outgoing traffic | 
**filters** | [**VpcFirewallRuleFilter**](VpcFirewallRuleFilter.md) | Reductions on the scope of the rule | 
**name** | **str** | Name of the rule, unique to this VPC | 
**priority** | **int** | The relative priority of this rule | 
**status** | [**VpcFirewallRuleStatus**](VpcFirewallRuleStatus.md) | Whether this rule is in effect | 
**targets** | [**List[VpcFirewallRuleTarget]**](VpcFirewallRuleTarget.md) | Determine the set of instances that the rule applies to | 

## Example

```python
from oxide.models.vpc_firewall_rule_update import VpcFirewallRuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleUpdate from a JSON string
vpc_firewall_rule_update_instance = VpcFirewallRuleUpdate.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleUpdate.to_json())

# convert the object into a dict
vpc_firewall_rule_update_dict = vpc_firewall_rule_update_instance.to_dict()
# create an instance of VpcFirewallRuleUpdate from a dict
vpc_firewall_rule_update_from_dict = VpcFirewallRuleUpdate.from_dict(vpc_firewall_rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


