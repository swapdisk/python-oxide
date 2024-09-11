# DiskCreate

Create-time parameters for a `Disk`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**disk_source** | [**DiskSource**](DiskSource.md) | initial source for this disk | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**size** | **int** | total size of the Disk in bytes | 

## Example

```python
from oxide.models.disk_create import DiskCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DiskCreate from a JSON string
disk_create_instance = DiskCreate.from_json(json)
# print the JSON string representation of the object
print(DiskCreate.to_json())

# convert the object into a dict
disk_create_dict = disk_create_instance.to_dict()
# create an instance of DiskCreate from a dict
disk_create_from_dict = DiskCreate.from_dict(disk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


