# InstanceNetworkInterfaceCreate

Create-time parameters for an `InstanceNetworkInterface`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**ip** | **str** | The IP address for the interface. One will be auto-assigned if not provided. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**subnet_name** | **str** | The VPC Subnet in which to create the interface. | 
**vpc_name** | **str** | The VPC in which to create the interface. | 

## Example

```python
from oxide.models.instance_network_interface_create import InstanceNetworkInterfaceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceCreate from a JSON string
instance_network_interface_create_instance = InstanceNetworkInterfaceCreate.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceCreate.to_json())

# convert the object into a dict
instance_network_interface_create_dict = instance_network_interface_create_instance.to_dict()
# create an instance of InstanceNetworkInterfaceCreate from a dict
instance_network_interface_create_from_dict = InstanceNetworkInterfaceCreate.from_dict(instance_network_interface_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


