# SwitchInterfaceConfigCreate

A layer-3 switch interface configuration. When IPv6 is enabled, a link local address will be created for the interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**SwitchInterfaceKind**](SwitchInterfaceKind.md) | What kind of switch interface this configuration represents. | 
**v6_enabled** | **bool** | Whether or not IPv6 is enabled. | 

## Example

```python
from oxide.models.switch_interface_config_create import SwitchInterfaceConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchInterfaceConfigCreate from a JSON string
switch_interface_config_create_instance = SwitchInterfaceConfigCreate.from_json(json)
# print the JSON string representation of the object
print(SwitchInterfaceConfigCreate.to_json())

# convert the object into a dict
switch_interface_config_create_dict = switch_interface_config_create_instance.to_dict()
# create an instance of SwitchInterfaceConfigCreate from a dict
switch_interface_config_create_from_dict = SwitchInterfaceConfigCreate.from_dict(switch_interface_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


