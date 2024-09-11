# AllowedSourceIpsOneOf1

Restrict access to a specific set of source IP addresses or subnets.  All others are prevented from reaching rack services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **str** |  | 
**ips** | [**List[IpNet]**](IpNet.md) |  | 

## Example

```python
from oxide.models.allowed_source_ips_one_of1 import AllowedSourceIpsOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedSourceIpsOneOf1 from a JSON string
allowed_source_ips_one_of1_instance = AllowedSourceIpsOneOf1.from_json(json)
# print the JSON string representation of the object
print(AllowedSourceIpsOneOf1.to_json())

# convert the object into a dict
allowed_source_ips_one_of1_dict = allowed_source_ips_one_of1_instance.to_dict()
# create an instance of AllowedSourceIpsOneOf1 from a dict
allowed_source_ips_one_of1_from_dict = AllowedSourceIpsOneOf1.from_dict(allowed_source_ips_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


