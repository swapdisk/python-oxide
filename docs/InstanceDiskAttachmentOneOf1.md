# InstanceDiskAttachmentOneOf1

During instance creation, attach this disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A disk name to attach | 
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_disk_attachment_one_of1 import InstanceDiskAttachmentOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDiskAttachmentOneOf1 from a JSON string
instance_disk_attachment_one_of1_instance = InstanceDiskAttachmentOneOf1.from_json(json)
# print the JSON string representation of the object
print(InstanceDiskAttachmentOneOf1.to_json())

# convert the object into a dict
instance_disk_attachment_one_of1_dict = instance_disk_attachment_one_of1_instance.to_dict()
# create an instance of InstanceDiskAttachmentOneOf1 from a dict
instance_disk_attachment_one_of1_from_dict = InstanceDiskAttachmentOneOf1.from_dict(instance_disk_attachment_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


