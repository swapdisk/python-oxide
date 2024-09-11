# VpcFirewallRuleHostFilter

The `VpcFirewallRuleHostFilter` is used to filter traffic on the basis of its source or destination host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**IpNet**](IpNet.md) |  | 

## Example

```python
from oxide.models.vpc_firewall_rule_host_filter import VpcFirewallRuleHostFilter

# TODO update the JSON string below
json = "{}"
# create an instance of VpcFirewallRuleHostFilter from a JSON string
vpc_firewall_rule_host_filter_instance = VpcFirewallRuleHostFilter.from_json(json)
# print the JSON string representation of the object
print(VpcFirewallRuleHostFilter.to_json())

# convert the object into a dict
vpc_firewall_rule_host_filter_dict = vpc_firewall_rule_host_filter_instance.to_dict()
# create an instance of VpcFirewallRuleHostFilter from a dict
vpc_firewall_rule_host_filter_from_dict = VpcFirewallRuleHostFilter.from_dict(vpc_firewall_rule_host_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


