# AllowListUpdate

Parameters for updating allowed source IPs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ips** | [**AllowedSourceIps**](AllowedSourceIps.md) | The new list of allowed source IPs. | 

## Example

```python
from oxide.models.allow_list_update import AllowListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AllowListUpdate from a JSON string
allow_list_update_instance = AllowListUpdate.from_json(json)
# print the JSON string representation of the object
print(AllowListUpdate.to_json())

# convert the object into a dict
allow_list_update_dict = allow_list_update_instance.to_dict()
# create an instance of AllowListUpdate from a dict
allow_list_update_from_dict = AllowListUpdate.from_dict(allow_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


