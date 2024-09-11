# SwitchPortSettingsGroups

This structure maps a port settings object to a port settings groups. Port settings objects may inherit settings from groups. This mapping defines the relationship between settings objects and the groups they reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_settings_group_id** | **str** | The id of a port settings group being referenced by a port settings object. | 
**port_settings_id** | **str** | The id of a port settings object referencing a port settings group. | 

## Example

```python
from oxide.models.switch_port_settings_groups import SwitchPortSettingsGroups

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchPortSettingsGroups from a JSON string
switch_port_settings_groups_instance = SwitchPortSettingsGroups.from_json(json)
# print the JSON string representation of the object
print(SwitchPortSettingsGroups.to_json())

# convert the object into a dict
switch_port_settings_groups_dict = switch_port_settings_groups_instance.to_dict()
# create an instance of SwitchPortSettingsGroups from a dict
switch_port_settings_groups_from_dict = SwitchPortSettingsGroups.from_dict(switch_port_settings_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


