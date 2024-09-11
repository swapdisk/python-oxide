# VpcSubnetCreate

Create-time parameters for a `VpcSubnet`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_router** | [**NameOrId**](NameOrId.md) | An optional router, used to direct packets sent from hosts in this subnet to any destination address.  Custom routers apply in addition to the VPC-wide *system* router, and have higher priority than the system router for an otherwise equal-prefix-length match. | [optional] 
**description** | **str** |  | 
**ipv4_block** | **str** | The IPv4 address range for this subnet.  It must be allocated from an RFC 1918 private address range, and must not overlap with any other existing subnet in the VPC. | 
**ipv6_block** | **str** | The IPv6 address range for this subnet.  It must be allocated from the RFC 4193 Unique Local Address range, with the prefix equal to the parent VPC&#39;s prefix. A random &#x60;/64&#x60; block will be assigned if one is not provided. It must not overlap with any existing subnet in the VPC. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.vpc_subnet_create import VpcSubnetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VpcSubnetCreate from a JSON string
vpc_subnet_create_instance = VpcSubnetCreate.from_json(json)
# print the JSON string representation of the object
print(VpcSubnetCreate.to_json())

# convert the object into a dict
vpc_subnet_create_dict = vpc_subnet_create_instance.to_dict()
# create an instance of VpcSubnetCreate from a dict
vpc_subnet_create_from_dict = VpcSubnetCreate.from_dict(vpc_subnet_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


