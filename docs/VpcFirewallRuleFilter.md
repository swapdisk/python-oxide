# VpcFirewallRuleFilter

Filters reduce the scope of a firewall rule. Without filters, the rule applies to all packets to the targets (or from the targets, if it's an outbound rule). With multiple filters, the rule applies only to packets matching ALL filters. The maximum number of each type of filter is 256.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[VpcFirewallRuleHostFilter]**](VpcFirewallRuleHostFilter.md) | If present, host filters match the \&quot;other end\&quot; of traffic from the target’s perspective: for an inbound rule, they match the source of traffic. For an outbound rule, they match the destination. | [optional] 
**ports** | **List[str]** | If present, the destination ports or port ranges this rule applies to. | [optional] 
**protocols** | [**List[VpcFirewallRuleProtocol]**](VpcFirewallRuleProtocol.md) | If present, the networking protocols this rule applies to. | [optional] 

## Example

```python
from oxide.models.vpc_firewall_rule_filter import VpcFirewallRuleFilter

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleFilter from a JSON string
vpc_firewall_rule_filter_instance = VpcFirewallRuleFilter.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleFilter.to_json())

# convert the object into a dict
vpc_firewall_rule_filter_dict = vpc_firewall_rule_filter_instance.to_dict()
# create an instance of VpcFirewallRuleFilter from a dict
vpc_firewall_rule_filter_from_dict = VpcFirewallRuleFilter.from_dict(vpc_firewall_rule_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


