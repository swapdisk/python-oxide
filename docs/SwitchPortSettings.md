# SwitchPortSettings

A switch port settings identity whose id may be used to view additional details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.switch_port_settings import SwitchPortSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortSettings from a JSON string
switch_port_settings_instance = SwitchPortSettings.from_json(json)
# print the JSON string representation of the object
print(SwitchPortSettings.to_json())

# convert the object into a dict
switch_port_settings_dict = switch_port_settings_instance.to_dict()
# create an instance of SwitchPortSettings from a dict
switch_port_settings_from_dict = SwitchPortSettings.from_dict(switch_port_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


