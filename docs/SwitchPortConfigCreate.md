# SwitchPortConfigCreate

Physical switch port configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**SwitchPortGeometry**](SwitchPortGeometry.md) | Link geometry for the switch port. | 

## Example

```python
from oxide.models.switch_port_config_create import SwitchPortConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortConfigCreate from a JSON string
switch_port_config_create_instance = SwitchPortConfigCreate.from_json(json)
# print the JSON string representation of the object
print(SwitchPortConfigCreate.to_json())

# convert the object into a dict
switch_port_config_create_dict = switch_port_config_create_instance.to_dict()
# create an instance of SwitchPortConfigCreate from a dict
switch_port_config_create_from_dict = SwitchPortConfigCreate.from_dict(switch_port_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


