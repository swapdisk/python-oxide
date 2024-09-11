# Switch

An operator's view of a Switch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseboard** | [**Baseboard**](Baseboard.md) |  | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**rack_id** | **str** | The rack to which this Switch is currently attached | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.switch import Switch

# TODO update the JSON string below
json = "{}"
# create an instance of Switch from a JSON string
switch_instance = Switch.from_json(json)
# print the JSON string representation of the object
print(Switch.to_json())

# convert the object into a dict
switch_dict = switch_instance.to_dict()
# create an instance of Switch from a dict
switch_from_dict = Switch.from_dict(switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


