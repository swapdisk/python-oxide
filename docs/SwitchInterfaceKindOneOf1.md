# SwitchInterfaceKindOneOf1

VLAN interfaces allow physical interfaces to be multiplexed onto multiple logical links, each distinguished by a 12-bit 802.1Q Ethernet tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**vid** | **int** | The virtual network id (VID) that distinguishes this interface and is used for producing and consuming 802.1Q Ethernet tags. This field has a maximum value of 4095 as 802.1Q tags are twelve bits. | 

## Example

```python
from oxide.models.switch_interface_kind_one_of1 import SwitchInterfaceKindOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInterfaceKindOneOf1 from a JSON string
switch_interface_kind_one_of1_instance = SwitchInterfaceKindOneOf1.from_json(json)
# print the JSON string representation of the object
print(SwitchInterfaceKindOneOf1.to_json())

# convert the object into a dict
switch_interface_kind_one_of1_dict = switch_interface_kind_one_of1_instance.to_dict()
# create an instance of SwitchInterfaceKindOneOf1 from a dict
switch_interface_kind_one_of1_from_dict = SwitchInterfaceKindOneOf1.from_dict(switch_interface_kind_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


