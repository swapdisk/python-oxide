# NetworkInterfaceKind

The type of network interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.network_interface_kind import NetworkInterfaceKind

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceKind from a JSON string
network_interface_kind_instance = NetworkInterfaceKind.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceKind.to_json())

# convert the object into a dict
network_interface_kind_dict = network_interface_kind_instance.to_dict()
# create an instance of NetworkInterfaceKind from a dict
network_interface_kind_from_dict = NetworkInterfaceKind.from_dict(network_interface_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


