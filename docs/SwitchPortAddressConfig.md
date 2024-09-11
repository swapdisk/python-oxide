# SwitchPortAddressConfig

An IP address configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**IpNet**](IpNet.md) | The IP address and prefix. | 
**address_lot_block_id** | **str** | The id of the address lot block this address is drawn from. | 
**interface_name** | **str** | The interface name this address belongs to. | 
**port_settings_id** | **str** | The port settings object this address configuration belongs to. | 
**vlan_id** | **int** | An optional VLAN ID | [optional] 

## Example

```python
from oxide.models.switch_port_address_config import SwitchPortAddressConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortAddressConfig from a JSON string
switch_port_address_config_instance = SwitchPortAddressConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchPortAddressConfig.to_json())

# convert the object into a dict
switch_port_address_config_dict = switch_port_address_config_instance.to_dict()
# create an instance of SwitchPortAddressConfig from a dict
switch_port_address_config_from_dict = SwitchPortAddressConfig.from_dict(switch_port_address_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


