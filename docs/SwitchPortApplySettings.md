# SwitchPortApplySettings

Parameters for applying settings to switch ports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_settings** | [**NameOrId**](NameOrId.md) | A name or id to use when applying switch port settings. | 

## Example

```python
from oxide.models.switch_port_apply_settings import SwitchPortApplySettings

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortApplySettings from a JSON string
switch_port_apply_settings_instance = SwitchPortApplySettings.from_json(json)
# print the JSON string representation of the object
print(SwitchPortApplySettings.to_json())

# convert the object into a dict
switch_port_apply_settings_dict = switch_port_apply_settings_instance.to_dict()
# create an instance of SwitchPortApplySettings from a dict
switch_port_apply_settings_from_dict = SwitchPortApplySettings.from_dict(switch_port_apply_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


