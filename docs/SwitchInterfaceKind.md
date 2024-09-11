# SwitchInterfaceKind

Indicates the kind for a switch interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**vid** | **int** | The virtual network id (VID) that distinguishes this interface and is used for producing and consuming 802.1Q Ethernet tags. This field has a maximum value of 4095 as 802.1Q tags are twelve bits. | 

## Example

```python
from oxide.models.switch_interface_kind import SwitchInterfaceKind

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInterfaceKind from a JSON string
switch_interface_kind_instance = SwitchInterfaceKind.from_json(json)
# print the JSON string representation of the object
print(SwitchInterfaceKind.to_json())

# convert the object into a dict
switch_interface_kind_dict = switch_interface_kind_instance.to_dict()
# create an instance of SwitchInterfaceKind from a dict
switch_interface_kind_from_dict = SwitchInterfaceKind.from_dict(switch_interface_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


