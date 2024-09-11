# SwitchPortConfig

A physical port configuration for a port settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**SwitchPortGeometry2**](SwitchPortGeometry2.md) | The physical link geometry of the port. | 
**port_settings_id** | **str** | The id of the port settings object this configuration belongs to. | 

## Example

```python
from oxide.models.switch_port_config import SwitchPortConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortConfig from a JSON string
switch_port_config_instance = SwitchPortConfig.from_json(json)
# print the JSON string representation of the object
print(SwitchPortConfig.to_json())

# convert the object into a dict
switch_port_config_dict = switch_port_config_instance.to_dict()
# create an instance of SwitchPortConfig from a dict
switch_port_config_from_dict = SwitchPortConfig.from_dict(switch_port_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


