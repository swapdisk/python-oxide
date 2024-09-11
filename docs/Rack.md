# Rack

View of an Rack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.rack import Rack

# TODO update the JSON string below
json = "{}"
# create an instance of Rack from a JSON string
rack_instance = Rack.from_json(json)
# print the JSON string representation of the object
print(Rack.to_json())

# convert the object into a dict
rack_dict = rack_instance.to_dict()
# create an instance of Rack from a dict
rack_from_dict = Rack.from_dict(rack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


