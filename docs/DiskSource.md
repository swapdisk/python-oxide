# DiskSource

Different sources for a disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | [**BlockSize**](BlockSize.md) |  | 
**type** | **str** |  | 
**snapshot_id** | **str** |  | 
**image_id** | **str** |  | 

## Example

```python
from oxide.models.disk_source import DiskSource

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSource from a JSON string
disk_source_instance = DiskSource.from_json(json)
# print the JSON string representation of the object
print(DiskSource.to_json())

# convert the object into a dict
disk_source_dict = disk_source_instance.to_dict()
# create an instance of DiskSource from a dict
disk_source_from_dict = DiskSource.from_dict(disk_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


