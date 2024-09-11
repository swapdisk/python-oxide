# InstanceNetworkInterfaceAttachmentOneOf1

The default networking configuration for an instance is to create a single primary interface with an automatically-assigned IP address. The IP will be pulled from the Project's default VPC / VPC Subnet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from oxide.models.instance_network_interface_attachment_one_of1 import InstanceNetworkInterfaceAttachmentOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceAttachmentOneOf1 from a JSON string
instance_network_interface_attachment_one_of1_instance = InstanceNetworkInterfaceAttachmentOneOf1.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceAttachmentOneOf1.to_json())

# convert the object into a dict
instance_network_interface_attachment_one_of1_dict = instance_network_interface_attachment_one_of1_instance.to_dict()
# create an instance of InstanceNetworkInterfaceAttachmentOneOf1 from a dict
instance_network_interface_attachment_one_of1_from_dict = InstanceNetworkInterfaceAttachmentOneOf1.from_dict(instance_network_interface_attachment_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


