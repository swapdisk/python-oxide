# SwitchInterfaceConfig

A switch port interface configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this switch interface. | 
**interface_name** | **str** | The name of this switch interface. | 
**kind** | [**SwitchInterfaceKind2**](SwitchInterfaceKind2.md) | The switch interface kind. | 
**port_settings_id** | **str** | The port settings object this switch interface configuration belongs to. | 
**v6_enabled** | **bool** | Whether or not IPv6 is enabled on this interface. | 

## Example

```python
from oxide.models.switch_interface_config import SwitchInterfaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInterfaceConfig from a JSON string
switch_interface_config_instance = SwitchInterfaceConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchInterfaceConfig.to_json())

# convert the object into a dict
switch_interface_config_dict = switch_interface_config_instance.to_dict()
# create an instance of SwitchInterfaceConfig from a dict
switch_interface_config_from_dict = SwitchInterfaceConfig.from_dict(switch_interface_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


