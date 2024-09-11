# InstanceNetworkInterfaceUpdate

Parameters for updating an `InstanceNetworkInterface`  Note that modifying IP addresses for an interface is not yet supported, a new interface must be created instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 
**primary** | **bool** | Make a secondary interface the instance&#39;s primary interface.  If applied to a secondary interface, that interface will become the primary on the next reboot of the instance. Note that this may have implications for routing between instances, as the new primary interface will be on a distinct subnet from the previous primary interface.  Note that this can only be used to select a new primary interface for an instance. Requests to change the primary interface into a secondary will return an error. | [optional] [default to False]
**transit_ips** | [**List[IpNet]**](IpNet.md) | A set of additional networks that this interface may send and receive traffic on. | [optional] [default to []]

## Example

```python
from oxide.models.instance_network_interface_update import InstanceNetworkInterfaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceNetworkInterfaceUpdate from a JSON string
instance_network_interface_update_instance = InstanceNetworkInterfaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InstanceNetworkInterfaceUpdate.to_json())

# convert the object into a dict
instance_network_interface_update_dict = instance_network_interface_update_instance.to_dict()
# create an instance of InstanceNetworkInterfaceUpdate from a dict
instance_network_interface_update_from_dict = InstanceNetworkInterfaceUpdate.from_dict(instance_network_interface_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


