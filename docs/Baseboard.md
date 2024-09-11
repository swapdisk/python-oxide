# Baseboard

Properties that uniquely identify an Oxide hardware component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part** | **str** |  | 
**revision** | **int** |  | 
**serial** | **str** |  | 

## Example

```python
from oxide.models.baseboard import Baseboard

# TODO update the JSON string below
json = "{}"
# create an instance of Baseboard from a JSON string
baseboard_instance = Baseboard.from_json(json)
# print the JSON string representation of the object
print(Baseboard.to_json())

# convert the object into a dict
baseboard_dict = baseboard_instance.to_dict()
# create an instance of Baseboard from a dict
baseboard_from_dict = Baseboard.from_dict(baseboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


