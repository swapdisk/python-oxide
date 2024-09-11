# NetworkInterfaceKindOneOf1

A vNIC associated with an internal service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.network_interface_kind_one_of1 import NetworkInterfaceKindOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceKindOneOf1 from a JSON string
network_interface_kind_one_of1_instance = NetworkInterfaceKindOneOf1.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceKindOneOf1.to_json())

# convert the object into a dict
network_interface_kind_one_of1_dict = network_interface_kind_one_of1_instance.to_dict()
# create an instance of NetworkInterfaceKindOneOf1 from a dict
network_interface_kind_one_of1_from_dict = NetworkInterfaceKindOneOf1.from_dict(network_interface_kind_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


