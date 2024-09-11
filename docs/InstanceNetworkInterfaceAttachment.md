# InstanceNetworkInterfaceAttachment

Describes an attachment of an `InstanceNetworkInterface` to an `Instance`, at the time the instance is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**List[InstanceNetworkInterfaceCreate]**](InstanceNetworkInterfaceCreate.md) |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_network_interface_attachment import InstanceNetworkInterfaceAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceAttachment from a JSON string
instance_network_interface_attachment_instance = InstanceNetworkInterfaceAttachment.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceAttachment.to_json())

# convert the object into a dict
instance_network_interface_attachment_dict = instance_network_interface_attachment_instance.to_dict()
# create an instance of InstanceNetworkInterfaceAttachment from a dict
instance_network_interface_attachment_from_dict = InstanceNetworkInterfaceAttachment.from_dict(instance_network_interface_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


