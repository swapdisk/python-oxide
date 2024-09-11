# VpcCreate

Create-time parameters for a `Vpc`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**dns_name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**ipv6_prefix** | **str** | The IPv6 prefix for this VPC  All IPv6 subnets created from this VPC must be taken from this range, which should be a Unique Local Address in the range &#x60;fd00::/48&#x60;. The default VPC Subnet will have the first &#x60;/64&#x60; range from this prefix. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.vpc_create import VpcCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VpcCreate from a JSON string
vpc_create_instance = VpcCreate.from_json(json)
# print the JSON string representation of the object
print(VpcCreate.to_json())

# convert the object into a dict
vpc_create_dict = vpc_create_instance.to_dict()
# create an instance of VpcCreate from a dict
vpc_create_from_dict = VpcCreate.from_dict(vpc_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


