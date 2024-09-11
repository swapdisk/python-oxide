# Cumulativedouble

A cumulative or counter data type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | 
**value** | **float** |  | 

## Example

```python
from oxide.models.cumulativedouble import Cumulativedouble

# TODO update the JSON string below
json = "{}"
# create an instance of Cumulativedouble from a JSON string
cumulativedouble_instance = Cumulativedouble.from_json(json)
# print the JSON string representation of the object
print(Cumulativedouble.to_json())

# convert the object into a dict
cumulativedouble_dict = cumulativedouble_instance.to_dict()
# create an instance of Cumulativedouble from a dict
cumulativedouble_from_dict = Cumulativedouble.from_dict(cumulativedouble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


