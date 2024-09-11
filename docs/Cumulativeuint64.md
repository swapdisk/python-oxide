# Cumulativeuint64

A cumulative or counter data type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | 
**value** | **int** |  | 

## Example

```python
from oxide.models.cumulativeuint64 import Cumulativeuint64

# TODO update the JSON string below
json = "{}"
# create an instance of Cumulativeuint64 from a JSON string
cumulativeuint64_instance = Cumulativeuint64.from_json(json)
# print the JSON string representation of the object
print(Cumulativeuint64.to_json())

# convert the object into a dict
cumulativeuint64_dict = cumulativeuint64_instance.to_dict()
# create an instance of Cumulativeuint64 from a dict
cumulativeuint64_from_dict = Cumulativeuint64.from_dict(cumulativeuint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


