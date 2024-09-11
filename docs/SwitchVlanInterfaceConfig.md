# SwitchVlanInterfaceConfig

A switch port VLAN interface configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_config_id** | **str** | The switch interface configuration this VLAN interface configuration belongs to. | 
**vlan_id** | **int** | The virtual network id for this interface that is used for producing and consuming 802.1Q Ethernet tags. This field has a maximum value of 4095 as 802.1Q tags are twelve bits. | 

## Example

```python
from oxide.models.switch_vlan_interface_config import SwitchVlanInterfaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchVlanInterfaceConfig from a JSON string
switch_vlan_interface_config_instance = SwitchVlanInterfaceConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchVlanInterfaceConfig.to_json())

# convert the object into a dict
switch_vlan_interface_config_dict = switch_vlan_interface_config_instance.to_dict()
# create an instance of SwitchVlanInterfaceConfig from a dict
switch_vlan_interface_config_from_dict = SwitchVlanInterfaceConfig.from_dict(switch_vlan_interface_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


