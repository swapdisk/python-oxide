# Cumulativeint64

A cumulative or counter data type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | 
**value** | **int** |  | 

## Example

```python
from oxide.models.cumulativeint64 import Cumulativeint64

# TODO update the JSON string below
json = "{}"
# create an instance of Cumulativeint64 from a JSON string
cumulativeint64_instance = Cumulativeint64.from_json(json)
# print the JSON string representation of the object
print(Cumulativeint64.to_json())

# convert the object into a dict
cumulativeint64_dict = cumulativeint64_instance.to_dict()
# create an instance of Cumulativeint64 from a dict
cumulativeint64_from_dict = Cumulativeint64.from_dict(cumulativeint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


