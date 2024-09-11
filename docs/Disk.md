# Disk

View of a Disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | Byte count to express memory or storage capacity. | 
**description** | **str** | human-readable free-form text about a resource | 
**device_path** | **str** |  | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**image_id** | **str** | ID of image from which disk was created, if any | [optional] 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**project_id** | **str** |  | 
**size** | **int** | Byte count to express memory or storage capacity. | 
**snapshot_id** | **str** | ID of snapshot from which disk was created, if any | [optional] 
**state** | [**DiskState**](DiskState.md) |  | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.disk import Disk

# TODO update the JSON string below
json = "{}"
# create an instance of Disk from a JSON string
disk_instance = Disk.from_json(json)
# print the JSON string representation of the object
print(Disk.to_json())

# convert the object into a dict
disk_dict = disk_instance.to_dict()
# create an instance of Disk from a dict
disk_from_dict = Disk.from_dict(disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


