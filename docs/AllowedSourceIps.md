# AllowedSourceIps

Description of source IPs allowed to reach rack services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **str** |  | 
**ips** | [**List[IpNet]**](IpNet.md) |  | 

## Example

```python
from oxide.models.allowed_source_ips import AllowedSourceIps

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedSourceIps from a JSON string
allowed_source_ips_instance = AllowedSourceIps.from_json(json)
# print the JSON string representation of the object
print(AllowedSourceIps.to_json())

# convert the object into a dict
allowed_source_ips_dict = allowed_source_ips_instance.to_dict()
# create an instance of AllowedSourceIps from a dict
allowed_source_ips_from_dict = AllowedSourceIps.from_dict(allowed_source_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


