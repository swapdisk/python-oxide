# InstanceDiskAttachment

Describe the instance's disks at creation time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**disk_source** | [**DiskSource**](DiskSource.md) | initial source for this disk | 
**name** | **str** | A disk name to attach | 
**size** | **int** | total size of the Disk in bytes | 
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_disk_attachment import InstanceDiskAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDiskAttachment from a JSON string
instance_disk_attachment_instance = InstanceDiskAttachment.from_json(json)
# print the JSON string representation of the object
print(InstanceDiskAttachment.to_json())

# convert the object into a dict
instance_disk_attachment_dict = instance_disk_attachment_instance.to_dict()
# create an instance of InstanceDiskAttachment from a dict
instance_disk_attachment_from_dict = InstanceDiskAttachment.from_dict(instance_disk_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


