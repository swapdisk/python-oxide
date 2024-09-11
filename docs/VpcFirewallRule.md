# VpcFirewallRule

A single rule in a VPC firewall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**VpcFirewallRuleAction**](VpcFirewallRuleAction.md) | Whether traffic matching the rule should be allowed or dropped | 
**description** | **str** | human-readable free-form text about a resource | 
**direction** | [**VpcFirewallRuleDirection**](VpcFirewallRuleDirection.md) | Whether this rule is for incoming or outgoing traffic | 
**filters** | [**VpcFirewallRuleFilter**](VpcFirewallRuleFilter.md) | Reductions on the scope of the rule | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**priority** | **int** | The relative priority of this rule | 
**status** | [**VpcFirewallRuleStatus**](VpcFirewallRuleStatus.md) | Whether this rule is in effect | 
**targets** | [**List[VpcFirewallRuleTarget]**](VpcFirewallRuleTarget.md) | Determine the set of instances that the rule applies to | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vpc_id** | **str** | The VPC to which this rule belongs | 

## Example

```python
from oxide.models.vpc_firewall_rule import VpcFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRule from a JSON string
vpc_firewall_rule_instance = VpcFirewallRule.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRule.to_json())

# convert the object into a dict
vpc_firewall_rule_dict = vpc_firewall_rule_instance.to_dict()
# create an instance of VpcFirewallRule from a dict
vpc_firewall_rule_from_dict = VpcFirewallRule.from_dict(vpc_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


