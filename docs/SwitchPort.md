# SwitchPort

A switch port represents a physical external port on a rack switch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the switch port. | 
**port_name** | **str** | The name of this switch port. | 
**port_settings_id** | **str** | The primary settings group of this switch port. Will be &#x60;None&#x60; until this switch port is configured. | [optional] 
**rack_id** | **str** | The rack this switch port belongs to. | 
**switch_location** | **str** | The switch location of this switch port. | 

## Example

```python
from oxide.models.switch_port import SwitchPort

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPort from a JSON string
switch_port_instance = SwitchPort.from_json(json)
# print the JSON string representation of the object
print(SwitchPort.to_json())

# convert the object into a dict
switch_port_dict = switch_port_instance.to_dict()
# create an instance of SwitchPort from a dict
switch_port_from_dict = SwitchPort.from_dict(switch_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


