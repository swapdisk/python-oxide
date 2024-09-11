# AllowList

Allowlist of IPs or subnets that can make requests to user-facing services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ips** | [**AllowedSourceIps**](AllowedSourceIps.md) | The allowlist of IPs or subnets. | 
**time_created** | **datetime** | Time the list was created. | 
**time_modified** | **datetime** | Time the list was last modified. | 

## Example

```python
from oxide.models.allow_list import AllowList

# TODO update the JSON string below
json = "{}"
# create an instance of AllowList from a JSON string
allow_list_instance = AllowList.from_json(json)
# print the JSON string representation of the object
print(AllowList.to_json())

# convert the object into a dict
allow_list_dict = allow_list_instance.to_dict()
# create an instance of AllowList from a dict
allow_list_from_dict = AllowList.from_dict(allow_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


