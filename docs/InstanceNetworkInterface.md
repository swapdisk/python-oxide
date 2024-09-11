# InstanceNetworkInterface

An `InstanceNetworkInterface` represents a virtual network interface device attached to an instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**instance_id** | **str** | The Instance to which the interface belongs. | 
**ip** | **str** | The IP address assigned to this interface. | 
**mac** | **str** | The MAC address assigned to this interface. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**primary** | **bool** | True if this interface is the primary for the instance to which it&#39;s attached. | 
**subnet_id** | **str** | The subnet to which the interface belongs. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**transit_ips** | [**List[IpNet]**](IpNet.md) | A set of additional networks that this interface may send and receive traffic on. | [optional] [default to []]
**vpc_id** | **str** | The VPC to which the interface belongs. | 

## Example

```python
from oxide.models.instance_network_interface import InstanceNetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterface from a JSON string
instance_network_interface_instance = InstanceNetworkInterface.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterface.to_json())

# convert the object into a dict
instance_network_interface_dict = instance_network_interface_instance.to_dict()
# create an instance of InstanceNetworkInterface from a dict
instance_network_interface_from_dict = InstanceNetworkInterface.from_dict(instance_network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


