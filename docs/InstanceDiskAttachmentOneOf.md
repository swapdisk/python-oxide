# InstanceDiskAttachmentOneOf

During instance creation, create and attach disks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**disk_source** | [**DiskSource**](DiskSource.md) | initial source for this disk | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**size** | **int** | total size of the Disk in bytes | 
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_disk_attachment_one_of import InstanceDiskAttachmentOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDiskAttachmentOneOf from a JSON string
instance_disk_attachment_one_of_instance = InstanceDiskAttachmentOneOf.from_json(json)
# print the JSON string representation of the object
print(InstanceDiskAttachmentOneOf.to_json())

# convert the object into a dict
instance_disk_attachment_one_of_dict = instance_disk_attachment_one_of_instance.to_dict()
# create an instance of InstanceDiskAttachmentOneOf from a dict
instance_disk_attachment_one_of_from_dict = InstanceDiskAttachmentOneOf.from_dict(instance_disk_attachment_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


