# InstanceNetworkInterfaceAttachmentOneOf

Create one or more `InstanceNetworkInterface`s for the `Instance`.  If more than one interface is provided, then the first will be designated the primary interface for the instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**List[InstanceNetworkInterfaceCreate]**](InstanceNetworkInterfaceCreate.md) |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_network_interface_attachment_one_of import InstanceNetworkInterfaceAttachmentOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceAttachmentOneOf from a JSON string
instance_network_interface_attachment_one_of_instance = InstanceNetworkInterfaceAttachmentOneOf.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceAttachmentOneOf.to_json())

# convert the object into a dict
instance_network_interface_attachment_one_of_dict = instance_network_interface_attachment_one_of_instance.to_dict()
# create an instance of InstanceNetworkInterfaceAttachmentOneOf from a dict
instance_network_interface_attachment_one_of_from_dict = InstanceNetworkInterfaceAttachmentOneOf.from_dict(instance_network_interface_attachment_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


