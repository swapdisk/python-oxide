# DiskPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**NameOrId**](NameOrId.md) | Name or ID of the disk | 

## Example

```python
from oxide.models.disk_path import DiskPath

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPath from a JSON string
disk_path_instance = DiskPath.from_json(json)
# print the JSON string representation of the object
print(DiskPath.to_json())

# convert the object into a dict
disk_path_dict = disk_path_instance.to_dict()
# create an instance of DiskPath from a dict
disk_path_from_dict = DiskPath.from_dict(disk_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


