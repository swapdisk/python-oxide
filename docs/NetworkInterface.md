# NetworkInterface

Information required to construct a virtual network interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ip** | **str** |  | 
**kind** | [**NetworkInterfaceKind**](NetworkInterfaceKind.md) |  | 
**mac** | **str** | A Media Access Control address, in EUI-48 format | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**primary** | **bool** |  | 
**slot** | **int** |  | 
**subnet** | [**IpNet**](IpNet.md) |  | 
**transit_ips** | [**List[IpNet]**](IpNet.md) |  | [optional] [default to []]
**vni** | **int** | A Geneve Virtual Network Identifier | 

## Example

```python
from oxide.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInterface.to_json())

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_from_dict = NetworkInterface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


