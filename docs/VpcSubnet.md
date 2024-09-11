# VpcSubnet

A VPC subnet represents a logical grouping for instances that allows network traffic between them, within a IPv4 subnetwork or optionally an IPv6 subnetwork.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_router_id** | **str** | ID for an attached custom router. | [optional] 
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**ipv4_block** | **str** | The IPv4 subnet CIDR block. | 
**ipv6_block** | **str** | The IPv6 subnet CIDR block. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vpc_id** | **str** | The VPC to which the subnet belongs. | 

## Example

```python
from oxide.models.vpc_subnet import VpcSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of VpcSubnet from a JSON string
vpc_subnet_instance = VpcSubnet.from_json(json)
# print the JSON string representation of the object
print(VpcSubnet.to_json())

# convert the object into a dict
vpc_subnet_dict = vpc_subnet_instance.to_dict()
# create an instance of VpcSubnet from a dict
vpc_subnet_from_dict = VpcSubnet.from_dict(vpc_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


