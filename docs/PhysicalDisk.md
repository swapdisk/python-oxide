# PhysicalDisk

View of a Physical Disk  Physical disks reside in a particular sled and are used to store both Instance Disk data as well as internal metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_factor** | [**PhysicalDiskKind**](PhysicalDiskKind.md) |  | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**model** | **str** |  | 
**policy** | [**PhysicalDiskPolicy**](PhysicalDiskPolicy.md) | The operator-defined policy for a physical disk. | 
**serial** | **str** |  | 
**sled_id** | **str** | The sled to which this disk is attached, if any. | [optional] 
**state** | [**PhysicalDiskState**](PhysicalDiskState.md) | The current state Nexus believes the disk to be in. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**vendor** | **str** |  | 

## Example

```python
from oxide.models.physical_disk import PhysicalDisk

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalDisk from a JSON string
physical_disk_instance = PhysicalDisk.from_json(json)
# print the JSON string representation of the object
print(PhysicalDisk.to_json())

# convert the object into a dict
physical_disk_dict = physical_disk_instance.to_dict()
# create an instance of PhysicalDisk from a dict
physical_disk_from_dict = PhysicalDisk.from_dict(physical_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


