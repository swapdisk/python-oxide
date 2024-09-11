# NetworkInterfaceKindOneOf

A vNIC attached to a guest instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.network_interface_kind_one_of import NetworkInterfaceKindOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceKindOneOf from a JSON string
network_interface_kind_one_of_instance = NetworkInterfaceKindOneOf.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceKindOneOf.to_json())

# convert the object into a dict
network_interface_kind_one_of_dict = network_interface_kind_one_of_instance.to_dict()
# create an instance of NetworkInterfaceKindOneOf from a dict
network_interface_kind_one_of_from_dict = NetworkInterfaceKindOneOf.from_dict(network_interface_kind_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


